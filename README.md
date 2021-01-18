# ndpretty
> Your little helper to display numpy ndarrays in a pretty table in Jupyter notebooks.


Jupyter notebooks are a great way to develop. `ndpretty` makes it even better for people who use numpy by providing nice formatting of `ndarray`s.

## Install

`pip install ndpretty`

## How to use

```python
import ndpretty
import numpy as np
```

Display an ndarray using `ndarray_html()`:

```python
ndpretty.ndarray_html(np.random.rand(3, 4))
```

<img src="img/2D.png" width="150px"/>

<!--<div style="overflow: auto"><table><tr><th></th><th>0</th><th>1</th><th>2</th><th>3</th></tr><tr><td><b>0</b></td><td style="background-color: #6e6eff">0.0685</td><td style="background-color: #905cc0">0.33993</td><td style="background-color: #7e65e0">0.19991</td><td style="background-color: #a75196">0.52213</td></tr><tr><td><b>1</b></td><td style="background-color: #7769ed">0.14278</td><td style="background-color: #bb4772">0.67834</td><td style="background-color: #8e5dc4">0.32163</td><td style="background-color: #8f5dc1">0.33468</td></tr><tr><td><b>2</b></td><td style="background-color: #b54a7d">0.63085</td><td style="background-color: #d53a42">0.88666</td><td style="background-color: #cb3f54">0.80842</td><td style="background-color: #dc3737">0.93526</td></tr></table></div>-->


If you want all `np.ndarray`s and `torch.Tensor`s to be automatically formatted like this, load the default configuration:

```python
ndpretty.default()
```

After this line has been exectued, all cell outputs that are `np.ndarray` or `torch.Tensor` are automatically formatted by ndpretty.

```python
a = np.random.rand(10, 5)
a
```

    10×5 float64 ndarray

<img src="img/2D_2.png" width="150px"/>

<!--<div style="overflow: auto"><table><tr><th></th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th></tr><tr><td><b>0</b></td><td style="background-color: #9d56a8">0.42592</td><td style="background-color: #ce3d4f">0.84211</td><td style="background-color: #9c56aa">0.41396</td><td style="background-color: #c34363">0.74758</td><td style="background-color: #9759b3">0.37527</td></tr><tr><td><b>1</b></td><td style="background-color: #cb3f55">0.8142</td><td style="background-color: #b7497a">0.64174</td><td style="background-color: #c24364">0.74288</td><td style="background-color: #da3739">0.94611</td><td style="background-color: #8d5ec6">0.28437</td></tr><tr><td><b>2</b></td><td style="background-color: #9a57ad">0.40014</td><td style="background-color: #b34b80">0.6139</td><td style="background-color: #ab4f8e">0.54594</td><td style="background-color: #8960cd">0.253</td><td style="background-color: #8761d1">0.23285</td></tr><tr><td><b>3</b></td><td style="background-color: #6f6dfb">0.032832</td><td style="background-color: #be456c">0.70744</td><td style="background-color: #8d5ec6">0.2851</td><td style="background-color: #c6415e">0.77141</td><td style="background-color: #ac4e8e">0.54845</td></tr><tr><td><b>4</b></td><td style="background-color: #c24365">0.73744</td><td style="background-color: #c8405a">0.79015</td><td style="background-color: #cf3d4d">0.85051</td><td style="background-color: #c24365">0.73791</td><td style="background-color: #a5529a">0.49018</td></tr><tr><td><b>5</b></td><td style="background-color: #8d5ec6">0.28515</td><td style="background-color: #915cbe">0.31936</td><td style="background-color: #8f5dc2">0.30216</td><td style="background-color: #8263da">0.19034</td><td style="background-color: #9c56aa">0.41642</td></tr><tr><td><b>6</b></td><td style="background-color: #8c5ec7">0.2805</td><td style="background-color: #da373a">0.94205</td><td style="background-color: #7d66e2">0.15212</td><td style="background-color: #dc3737">0.95743</td><td style="background-color: #ae4d89">0.5717</td></tr><tr><td><b>7</b></td><td style="background-color: #8661d3">0.22345</td><td style="background-color: #bf456a">0.71631</td><td style="background-color: #c04469">0.72249</td><td style="background-color: #b94875">0.66506</td><td style="background-color: #7c66e3">0.14654</td></tr><tr><td><b>8</b></td><td style="background-color: #8761d0">0.23784</td><td style="background-color: #c14466">0.73345</td><td style="background-color: #955ab6">0.35748</td><td style="background-color: #8661d1">0.23125</td><td style="background-color: #c8405a">0.7912</td></tr><tr><td><b>9</b></td><td style="background-color: #a95092">0.53008</td><td style="background-color: #d03c4c">0.85854</td><td style="background-color: #cd3e51">0.83361</td><td style="background-color: #d13c4a">0.86625</td><td style="background-color: #6e6eff">0.018584</td></tr></table></div>-->





    



It works with all numpy dtypes, multi-dimensional arrays and PyTorch tensors.

Find more usage examples [here](https://deutschmn.github.io/ndpretty/ndpretty.html#Example-usages).

## Why?

Look at the [alternatives](https://deutschmn.github.io/ndpretty/alternatives.html).

## Author

Patrick Deutschmann ([patrick@deutschmann.xyz](mailto:patrick@deutschmann.xyz))
