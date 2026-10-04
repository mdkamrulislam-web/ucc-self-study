#!/usr/bin/env python3
"""Run every runnable Python example in a guide and compare it with the output shown under it.

Usage:
    python3 tools/check_examples.py cs1068/index.html

An example is a <pre class="py" data-run> block (HTML-escaped code). If the next element is a
<pre class="out">, its text must match what the code prints. data-stdin="a&#10;b" supplies the
answers to input() calls; prompts and typed answers are echoed as a terminal would show them.
<pre class="out err"> expects an error: the last line of the traceback must match.
A trailing "  #!!" on a code line only marks it red on the page and is ignored here.
"""
import builtins, contextlib, html, io, re, sys, traceback
from html.parser import HTMLParser

src = open(sys.argv[1], encoding='utf-8').read()

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []; self.cur = None; self.depth = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'pre':
            cls = (a.get('class') or '').split()
            self.cur = {'kind': 'py' if 'py' in cls else 'out' if 'out' in cls else 'other',
                        'run': 'data-run' in a, 'stdin': a.get('data-stdin', ''), 'err': 'err' in cls, 'text': ''}
        elif self.cur is None and tag not in ('br',):
            self.items.append({'kind': 'tag'})
    def handle_endtag(self, tag):
        if tag == 'pre' and self.cur is not None:
            self.items.append(self.cur); self.cur = None
        elif self.cur is None:
            self.items.append({'kind': 'tag'})
    def handle_data(self, d):
        if self.cur is not None: self.cur['text'] += d
        elif d.strip(): self.items.append({'kind': 'text'})

p = P(); p.feed(src)
items = p.items
fails = runs = 0
for i, it in enumerate(items):
    if it['kind'] != 'py' or not it['run']:
        continue
    code = re.sub(r'\s*#!!\s*$', '', it['text'], flags=re.M)
    nxt = items[i + 1] if i + 1 < len(items) else None
    expected = nxt['text'] if nxt and nxt['kind'] == 'out' else None
    answers = iter(it['stdin'].split('\n'))
    buf = io.StringIO()
    def fake_input(prompt=''):
        v = next(answers)
        buf.write(str(prompt) + v + '\n')
        return v
    old = builtins.input; builtins.input = fake_input
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(code, 'main.py', 'exec'), {'__name__': '__main__'})
    except Exception as e:
        buf.write('ERROR ' + ''.join(traceback.format_exception_only(type(e), e)).strip().split('\n')[-1])
    finally:
        builtins.input = old
    got = buf.getvalue()
    runs += 1
    if expected is None:
        print('-- no expected output for:', code.splitlines()[0][:60])
        continue
    exp = expected
    if nxt['err']:
        exp_last = exp.strip().split('\n')[-1]
        exp_pre = exp.split('Traceback')[0] if 'Traceback' in exp else ''
        got_err = got.split('ERROR ')
        ok = len(got_err) == 2 and got_err[1].strip() == exp_last.strip() and got_err[0].rstrip() == exp_pre.rstrip() if 'File' in exp else False
        if not ok and 'SyntaxError' in exp_last:
            ok = len(got_err) == 2 and got_err[1].split(':')[0] == 'SyntaxError'
    else:
        ok = got.rstrip('\n') == exp.rstrip('\n')
    if not ok:
        fails += 1
        print('=' * 60); print(code); print('--- expected'); print(repr(exp)); print('--- got'); print(repr(got))
print(f'{runs} examples run, {fails} mismatches')
