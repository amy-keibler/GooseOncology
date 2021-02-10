{%- if include_emoji %}
import emoji
{%- endif %}

def hello(name="World"):
{%- if include_emoji %}
  return emoji.emojize(f"Hello, {name} :wave:", use_aliases=True)
{%- else %}
  return f"Hello, {name}"
{%- endif %}