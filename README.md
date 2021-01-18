# Welcome to `ndpretty`
> Your little helper to display numpy ndarrays in a pretty table in Jupyter notebooks.


Jupyter notebooks are a great way to develop. `ndpretty` makes it even better for people who use numpy by providing nice formatting of `ndarray`s.

## Install

`pip install ndpretty`

## How to use

The default configuration is loaded as simply as this:

```
ndpretty.default()
```

After this line has been exectued, all cell outputs that are `np.ndarray` or `torch.Tensor` are automatically formatted by ndpretty.

```
a = np.random.rand(20, 30, 2)
a
```

    20×30×2 float64 ndarray





    



## Why?

Normally, `ndarray`s look like this in a Jupyter notebook:

```
a = np.random.rand(20, 30, 2)
print(a)
```

    [[[0.67332527 0.34687068]
      [0.38336068 0.34281941]
      [0.1953115  0.2203909 ]
      ...
      [0.41523347 0.14889802]
      [0.35095522 0.27271219]
      [0.93926387 0.83926031]]
    
     [[0.19346472 0.07249269]
      [0.55515394 0.25984324]
      [0.05044609 0.07408243]
      ...
      [0.22227792 0.93505193]
      [0.13283968 0.36381562]
      [0.78231665 0.40666018]]
    
     [[0.60423577 0.56197322]
      [0.264191   0.13435128]
      [0.26342234 0.43812004]
      ...
      [0.91436535 0.73497115]
      [0.51160691 0.4990356 ]
      [0.03899651 0.31745117]]
    
     ...
    
     [[0.89763993 0.74951795]
      [0.1901834  0.18405086]
      [0.90574303 0.67517041]
      ...
      [0.38670804 0.92472416]
      [0.4938217  0.6947183 ]
      [0.0836607  0.93746114]]
    
     [[0.25596595 0.90138221]
      [0.47579009 0.62427661]
      [0.88145006 0.20649818]
      ...
      [0.62222373 0.83292506]
      [0.6138533  0.1446508 ]
      [0.72526005 0.71392611]]
    
     [[0.07450451 0.84449197]
      [0.04629121 0.30654866]
      [0.51159759 0.94059547]
      ...
      [0.11555924 0.28475242]
      [0.40253806 0.34814258]
      [0.75509527 0.95187282]]]


At least to me, that's quite hard to read. Using `ndpretty` they look like this:

```
np.random.rand(10, 20)
```

    10×20 float64 ndarray



<div style="overflow: auto"><table><tr><th></th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th></tr><tr><td><b>0</b></td><td style="background-color: #c5425f">0.7994</td><td style="background-color: #a253a0">0.47513</td><td style="background-color: #da3739">0.98548</td><td style="background-color: #c7415c">0.81449</td><td style="background-color: #8f5dc2">0.30469</td><td style="background-color: #945ab8">0.3548</td><td style="background-color: #8c5ec8">0.2751</td><td style="background-color: #c14466">0.76199</td><td style="background-color: #7e65e1">0.14834</td><td style="background-color: #905cc0">0.31334</td><td style="background-color: #8761d1">0.23142</td><td style="background-color: #7d66e3">0.13961</td><td style="background-color: #a55299">0.51022</td><td style="background-color: #b14c84">0.61541</td><td style="background-color: #6f6dfc">0.015007</td><td style="background-color: #706cfb">0.021974</td><td style="background-color: #9e55a7">0.43819</td><td style="background-color: #9659b5">0.36991</td><td style="background-color: #d23b48">0.91109</td><td style="background-color: #9a57ae">0.40542</td></tr><tr><td><b>1</b></td><td style="background-color: #8860ce">0.24573</td><td style="background-color: #bd466e">0.72243</td><td style="background-color: #9659b6">0.36621</td><td style="background-color: #8562d3">0.21878</td><td style="background-color: #8f5dc2">0.30645</td><td style="background-color: #7b67e6">0.12406</td><td style="background-color: #cb3f55">0.84959</td><td style="background-color: #bf456a">0.74187</td><td style="background-color: #d7393f">0.95594</td><td style="background-color: #8860cf">0.24149</td><td style="background-color: #c94059">0.83017</td><td style="background-color: #7e65e0">0.15284</td><td style="background-color: #b84877">0.67774</td><td style="background-color: #d9383c">0.97464</td><td style="background-color: #925bbc">0.33628</td><td style="background-color: #d63941">0.94707</td><td style="background-color: #8c5ec6">0.28255</td><td style="background-color: #ab4f8e">0.56285</td><td style="background-color: #b34b80">0.63444</td><td style="background-color: #a65198">0.51469</td></tr><tr><td><b>2</b></td><td style="background-color: #945ab9">0.35053</td><td style="background-color: #b54a7d">0.65022</td><td style="background-color: #9a57ae">0.40593</td><td style="background-color: #ae4d89">0.58642</td><td style="background-color: #7a67e9">0.11277</td><td style="background-color: #b74978">0.67112</td><td style="background-color: #9759b3">0.37915</td><td style="background-color: #746af3">0.060156</td><td style="background-color: #8562d4">0.21737</td><td style="background-color: #d9383a">0.98055</td><td style="background-color: #d33b45">0.92675</td><td style="background-color: #8e5dc4">0.29508</td><td style="background-color: #ca3f56">0.84043</td><td style="background-color: #736bf4">0.054722</td><td style="background-color: #9858b2">0.38469</td><td style="background-color: #a154a1">0.4695</td><td style="background-color: #b34b80">0.63104</td><td style="background-color: #925bbc">0.33458</td><td style="background-color: #a054a3">0.45742</td><td style="background-color: #7f65df">0.16154</td></tr><tr><td><b>3</b></td><td style="background-color: #706cfa">0.024984</td><td style="background-color: #8263da">0.18527</td><td style="background-color: #7c66e3">0.13851</td><td style="background-color: #d33b47">0.91919</td><td style="background-color: #7f65e0">0.15738</td><td style="background-color: #8164db">0.17959</td><td style="background-color: #726bf6">0.043776</td><td style="background-color: #9958b0">0.39453</td><td style="background-color: #a4529c">0.49554</td><td style="background-color: #ce3d4f">0.87637</td><td style="background-color: #9759b3">0.37741</td><td style="background-color: #a3539e">0.48447</td><td style="background-color: #8164da">0.18364</td><td style="background-color: #cb3f54">0.85369</td><td style="background-color: #a4529b">0.49755</td><td style="background-color: #b04c85">0.60828</td><td style="background-color: #b04c85">0.60679</td><td style="background-color: #ad4e8b">0.57978</td><td style="background-color: #c04469">0.75004</td><td style="background-color: #a3539d">0.49046</td></tr><tr><td><b>4</b></td><td style="background-color: #8960cd">0.24986</td><td style="background-color: #9659b5">0.36831</td><td style="background-color: #cb3f54">0.85384</td><td style="background-color: #ca3f56">0.84131</td><td style="background-color: #c6415d">0.80605</td><td style="background-color: #925bbb">0.33801</td><td style="background-color: #6f6dfc">0.016675</td><td style="background-color: #c7415c">0.81101</td><td style="background-color: #d43a45">0.92752</td><td style="background-color: #b44a7e">0.6445</td><td style="background-color: #8263d8">0.19309</td><td style="background-color: #9958b0">0.3938</td><td style="background-color: #d23b48">0.91283</td><td style="background-color: #c34363">0.77922</td><td style="background-color: #756af1">0.070514</td><td style="background-color: #9759b3">0.37886</td><td style="background-color: #dc3737">0.99972</td><td style="background-color: #8860cf">0.24086</td><td style="background-color: #706cfb">0.022817</td><td style="background-color: #cf3d4d">0.88765</td></tr><tr><td><b>5</b></td><td style="background-color: #c44261">0.78628</td><td style="background-color: #ab4f8f">0.561</td><td style="background-color: #bd466e">0.72424</td><td style="background-color: #d53a42">0.93997</td><td style="background-color: #9d56a8">0.4338</td><td style="background-color: #b6497b">0.66026</td><td style="background-color: #7868eb">0.10236</td><td style="background-color: #726bf7">0.042229</td><td style="background-color: #7e65e0">0.15696</td><td style="background-color: #7e65e1">0.15063</td><td style="background-color: #d53a42">0.94084</td><td style="background-color: #8d5ec5">0.29141</td><td style="background-color: #955ab6">0.36513</td><td style="background-color: #d8383d">0.96494</td><td style="background-color: #c14466">0.7611</td><td style="background-color: #8e5dc3">0.30132</td><td style="background-color: #bf456a">0.74327</td><td style="background-color: #ce3d4f">0.87622</td><td style="background-color: #ba4774">0.69343</td><td style="background-color: #d7393e">0.96062</td></tr><tr><td><b>6</b></td><td style="background-color: #8462d6">0.20491</td><td style="background-color: #8363d7">0.20228</td><td style="background-color: #9c56aa">0.42382</td><td style="background-color: #8761cf">0.23811</td><td style="background-color: #7868ec">0.097497</td><td style="background-color: #bb4772">0.70397</td><td style="background-color: #d9383b">0.97805</td><td style="background-color: #9a57ae">0.40257</td><td style="background-color: #b54a7c">0.65107</td><td style="background-color: #ab4f8f">0.55942</td><td style="background-color: #8661d3">0.22066</td><td style="background-color: #d53a42">0.94207</td><td style="background-color: #7968ea">0.10526</td><td style="background-color: #955ab8">0.35672</td><td style="background-color: #8d5ec5">0.28866</td><td style="background-color: #ce3d4f">0.87569</td><td style="background-color: #ce3d4f">0.87632</td><td style="background-color: #a054a2">0.46516</td><td style="background-color: #c14467">0.75913</td><td style="background-color: #a55299">0.50887</td></tr><tr><td><b>7</b></td><td style="background-color: #d03c4b">0.89688</td><td style="background-color: #945ab8">0.35394</td><td style="background-color: #ca3f57">0.83786</td><td style="background-color: #bb4771">0.70679</td><td style="background-color: #d63940">0.95298</td><td style="background-color: #7868ec">0.095472</td><td style="background-color: #bf456b">0.73866</td><td style="background-color: #d9383c">0.97277</td><td style="background-color: #6e6eff">0.0032267</td><td style="background-color: #c6415d">0.80876</td><td style="background-color: #8462d5">0.2102</td><td style="background-color: #d03c4c">0.89178</td><td style="background-color: #cc3e52">0.86258</td><td style="background-color: #8363d8">0.19479</td><td style="background-color: #726bf6">0.045423</td><td style="background-color: #a85093">0.5377</td><td style="background-color: #d53a42">0.94481</td><td style="background-color: #af4d87">0.599</td><td style="background-color: #d43a45">0.92984</td><td style="background-color: #c24364">0.7721</td></tr><tr><td><b>8</b></td><td style="background-color: #a75197">0.51962</td><td style="background-color: #cd3e50">0.87225</td><td style="background-color: #945ab8">0.35578</td><td style="background-color: #a65197">0.51735</td><td style="background-color: #a65197">0.51886</td><td style="background-color: #8960cc">0.25257</td><td style="background-color: #cc3e53">0.85836</td><td style="background-color: #8263d9">0.19078</td><td style="background-color: #c7415b">0.81723</td><td style="background-color: #c84059">0.82564</td><td style="background-color: #a75196">0.52477</td><td style="background-color: #c6415d">0.80565</td><td style="background-color: #ae4d8a">0.58539</td><td style="background-color: #da373a">0.98297</td><td style="background-color: #cb3f54">0.85072</td><td style="background-color: #716cf8">0.033246</td><td style="background-color: #d63941">0.94552</td><td style="background-color: #d33b46">0.92084</td><td style="background-color: #a2539f">0.47969</td><td style="background-color: #6e6dfe">0.003909</td></tr><tr><td><b>9</b></td><td style="background-color: #915cbe">0.32696</td><td style="background-color: #d23b47">0.91614</td><td style="background-color: #c7415b">0.81576</td><td style="background-color: #b34b81">0.62993</td><td style="background-color: #d53a42">0.94406</td><td style="background-color: #db3737">0.99699</td><td style="background-color: #7b67e7">0.12138</td><td style="background-color: #7a67e9">0.11266</td><td style="background-color: #b44a7f">0.64038</td><td style="background-color: #c44261">0.78891</td><td style="background-color: #ab4f8e">0.56295</td><td style="background-color: #c34363">0.77601</td><td style="background-color: #9659b5">0.37037</td><td style="background-color: #bb4771">0.70828</td><td style="background-color: #756af1">0.072578</td><td style="background-color: #d7393f">0.95779</td><td style="background-color: #a154a2">0.46526</td><td style="background-color: #d53a42">0.94115</td><td style="background-color: #d03c4b">0.89678</td><td style="background-color: #b44a7e">0.64525</td></tr></table></div>





    



## Author

Patrick Deutschmann ([patrick@deutschmann.xyz](mailto:patrick@deutschmann.xyz))