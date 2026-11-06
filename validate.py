#!/usr/bin/env python3
"""Validate the articles JSON using only the Python standard library."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
path = root / 'data' / 'articles.json'
errors = []
try:
    articles = json.loads(path.read_text(encoding='utf-8'))
except (OSError, ValueError) as exc:
    raise SystemExit(f'FAIL: cannot read JSON: {exc}')
if not isinstance(articles, list) or not articles:
    raise SystemExit('FAIL: articles.json must be a non-empty array')
seen = set()
keys = {'slug', 'title', 'category', 'level', 'summary', 'readingMinutes', 'sections', 'sources'}
for i, a in enumerate(articles, 1):
    where = f'article[{i}]'
    if not isinstance(a, dict):
        errors.append(f'{where}: must be an object')
        continue
    for key in keys - a.keys():
        errors.append(f'{where}: missing {key}')
    slug = a.get('slug', '')
    if not isinstance(slug, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        errors.append(f'{where}: invalid slug')
    if slug in seen:
        errors.append(f'{where}: duplicate slug {slug}')
    seen.add(slug)
    for field in ('title', 'category', 'summary'):
        if not isinstance(a.get(field), str) or not a[field].strip():
            errors.append(f'{where}: {field} must be non-empty')
    if a.get('level') not in ('入門', '中階', '實務'):
        errors.append(f'{where}: invalid level')
    if type(a.get('readingMinutes')) is not int or not 1 <= a['readingMinutes'] <= 30:
        errors.append(f'{where}: readingMinutes must be an integer 1..30')
    sections = a.get('sections')
    if not isinstance(sections, list) or len(sections) < 2:
        errors.append(f'{where}: at least two sections required')
    else:
        for j, s in enumerate(sections, 1):
            if not isinstance(s, dict) or not isinstance(s.get('heading'), str) or not s['heading'].strip() or not isinstance(s.get('paragraphs'), list) or not s['paragraphs'] or any(not isinstance(p, str) or not p.strip() for p in s['paragraphs']):
                errors.append(f'{where}: section[{j}] invalid')
    sources = a.get('sources')
    if not isinstance(sources, list) or not sources:
        errors.append(f'{where}: at least one source required')
    else:
        for j, s in enumerate(sources, 1):
            if not isinstance(s, dict) or not isinstance(s.get('label'), str) or not s['label'].strip() or not isinstance(s.get('url'), str) or urlparse(s['url']).scheme != 'https' or not urlparse(s['url']).netloc:
                errors.append(f'{where}: source[{j}] invalid HTTPS URL/label')
if errors:
    print('\n'.join('FAIL: ' + err for err in errors))
    raise SystemExit(1)
print(f'PASS: {len(articles)} articles, unique slugs and valid schema/sources')
