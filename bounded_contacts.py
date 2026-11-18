"""Bounded extraction of addresses actually present in text or mailto links."""
import html,re
from bs4 import BeautifulSoup
EMAIL=re.compile(r'(?i)(?<![\w.!#$%&\x27*+/=?^_`{|}~-])([a-z0-9.!#$%&\x27*+/=?^_`{|}~-]{1,64}@[a-z0-9.-]{1,253}\.[a-z]{2,24})(?![\w.-])')
def extract_emails(value,domain=''):
 if re.search(r'(?i)<(?:html|body|div|a|script|img|span)\b',value[:4000]):
  s=BeautifulSoup(value[:2000000],'html.parser')
  for node in s(['script','style','noscript','svg']):node.decompose()
  links=[str(a['href'])[:2048] for a in s.find_all('a',href=True) if str(a['href']).lower().startswith('mailto:')][:200]
  value=s.get_text(' ',strip=True)[:500000]+' '+' '.join(links)
 decoded=html.unescape(value[:600000]).replace('(at)','@').replace('[at]','@')
 emails={m.lower().strip('.,;:') for m in EMAIL.findall(decoded)}
 return sorted(e for e in emails if e.rsplit('.',1)[-1] not in {'png','jpg','jpeg','gif','webp','svg','avif'} and e.rsplit('@',1)[-1] not in {'example.com','example.org','domain.com','yourdomain.com','test.com'})
