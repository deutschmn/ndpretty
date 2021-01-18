# AUTOGENERATED! DO NOT EDIT! File to edit: 00_ndpretty.ipynb (unless otherwise specified).

__all__ = ['lowest_color', 'highest_color', 'number_format', 'ndarray_html', 'register_formatter',
           'ndarray_stats_print_formatter', 'no_print_formatter', 'register_ndarray_formatter', 'torch_tensor_html',
           'tensor_stats_print_formatter', 'register_torch_tensor_formatter', 'default']

# Cell
import numpy as np
from sys import modules

import IPython
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

# Cell
lowest_color = (110, 110, 255)
highest_color = (220, 55, 55)

number_format = '%.5g'

# Cell
def ndarray_html(a):
    assert type(np.array([])) == np.ndarray, 'Only numpy ndarrays are supported'

    if len(a.shape) == 1:
        if a.shape[0] == 0:
            print('[]')
            return
        _html_array(a[:,np.newaxis])
    elif len(a.shape) == 2:
        _html_array(a)
    elif len(a.shape) > 2:
        d = len(a.shape)
        slice_str = "[:, :, " + "0, " * (d - 3) + "0]"
        slice_widget = widgets.Text(
            value=slice_str,
            placeholder="e.g. " + slice_str,
            description='Slice:',
            disabled=False
        )
        interact(_html_higher_d_array, a=fixed(a), slice_str=slice_widget)

def _to_HTML(a, alphas, is_numeric, lowest_color, highest_color):
    html = '<div style="overflow: auto">'
    html += '<table>'
    html += '<tr>'
    html += '<th></th>'
    for j in range(a.shape[1]):
        html += f'<th>{j}</th>'
    html += '</tr>'

    for i in range(a.shape[0]):
        html += "<tr>"
        html += f'<td><b>{i}</b></td>'
        for j in range(a.shape[1]):
            alpha = alphas[i][j]
            rgb_color = tuple((alpha * np.array(highest_color) + (1 - alpha) * np.array(lowest_color)).astype(np.uint8))
            hex_color = '#%02x%02x%02x' % rgb_color
            if is_numeric:
                value = number_format % a[i][j]
            else:
                value = str(a[i][j])
            html += '<td style="background-color: %s">%s</td>' % (hex_color, value)
        html += "</tr>"
    html += '</table>'
    html += '</div>'
    return html

def _html_higher_d_array(a, slice_str):
    try:
        sliced_a = eval("a" + slice_str)
        assert len(sliced_a.shape) == 2, "didn't slice down to 2D"
        _html_array(sliced_a)
    except Exception as e:
        print("Invalid slice: " + str(e))

def _html_array(a):
    is_numeric = np.issubdtype(a.dtype, np.number)

    if is_numeric:
        a_range = a.max() - a.min()
        if a_range == 0:
            alphas = np.zeros_like(a, dtype=np.float) + 0.5
        else:
            alphas = (a - a.min()) / a_range
    elif np.issubdtype(a.dtype, np.bool_):
        alphas = a.astype(np.float)
    else:
        alphas = np.zeros_like(a, dtype=np.float) + 0.5

    html = _to_HTML(a, alphas, is_numeric, lowest_color, highest_color)
    IPython.core.display.display(IPython.display.HTML(html))

# Cell
def register_formatter(dtype, html_formatter, print_formatter=None):
    formatters = get_ipython().display_formatter.formatters

    formatters['text/html'].for_type(dtype, html_formatter)
    if print_formatter is not None:
        formatters['text/plain'].for_type(dtype, print_formatter)

# Cell
def ndarray_stats_print_formatter(x, _, __):
    print('×'.join(map(str, x.shape)) + " " + str(x.dtype) + ' ndarray')

def no_print_formatter(x, _, __):
    return

def register_ndarray_formatter(print_formatter=ndarray_stats_print_formatter):
    register_formatter(np.ndarray, ndarray_html, print_formatter)

# Cell
def torch_tensor_html(t):
    ndarray_html(t.numpy())

def tensor_stats_print_formatter(x, _, __):
    print('×'.join(map(str, x.shape)) + " " + str(x.dtype) + ' tensor')

def register_torch_tensor_formatter(print_formatter=tensor_stats_print_formatter):
    register_formatter(torch.Tensor, torch_tensor_html, print_formatter)

# Cell
def default():
    register_ndarray_formatter()
    if 'torch' in modules:
        register_torch_tensor_formatter()