from {{project_name }}.lib import hello

def test_hello():
  assert "Hello, World{% if include_emoji %} 👋{% endif %}" == hello()

def test_hello_args():
  assert "Hello, {{ project_name }}{% if include_emoji %} 👋{% endif %}" == hello("{{ project_name }}")