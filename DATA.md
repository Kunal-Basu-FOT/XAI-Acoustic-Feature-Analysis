# Data access and layout

The voice recordings and derived per-recording feature spreadsheets are not
part of this repository. Access to recordings collected from students requires
the original study's authorization and consent terms.

The notebook expects a working folder with `RawSamples/<speaker>/*.wav` and
creates `ReSampled/`, `Filtered_Samples/`, `training/`, `testing/`,
`train_features.xlsx`, and `test_features.xlsx`. Each folder label is used as
the speaker class. Its original root path is hard-coded; replace it before a
local rerun. The released result table can be inspected without these data.
