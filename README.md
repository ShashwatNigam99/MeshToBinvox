# MeshToBinvox

## Converts mesh to binvox 
### (Output .mat format for current use case)

## Current support :
Will parse Wavefront OBJ, Geomview OFF, Autocad DXF, PLY and STL, if they contain polygons only.

## Usage
```python
python3 converter.py <path to mesh file>
```
This will save the corresponding .mat file in the output folder.

Example:
```python
python3 converter.py test.obj
```


## Credits:
### For conversion from mesh to voxels:
https://www.patrickmin.com/binvox/
### For reading/writing bonvox
https://github.com/dimatura/binvox-rw-py