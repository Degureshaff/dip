from django.shortcuts import render


def main(request):
  return render(request, 'index.html')

def one_python_download(request):
  return render(request, '1-python-download.html')

def two_idle_program(request):
  return render(request, '2-idle-program.html')

def three_python_syntax(request):
  return render(request, '3-python-syntax.html')

def four_if_else(request):
  return render(request, '4-if-else.html')

def five_loops(request):
  return render(request, '5-loops.html')

def six_keywords(request):
  return render(request, '6-keywords.html')

def seven_functions(request):
  return render(request, '7-functions.html')

def eight_numbers(request):
  return render(request, '8-int-float.html')


def nine_lists(request):
  return render(request, '9-lists.html')


def ten_indexes(request):
  return render(request, '10-indexes.html')


def eleven_tuples(request):
  return render(request, '11-tuples.html')


def twelve_dicts(request):
  return render(request, '12-dicts.html')


def thirteen_sets(request):
  return render(request, '13-sets.html')

def fourteen_def(request):
  return render(request, '14-def.html')

def fifteen_os(request):
  return render(request, '15-os.html')

def error404(request):
  return render(request, '404.html')