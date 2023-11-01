# Datasets

To download dataset files, check out the "Public" and "Private" sections to the left. Please note that you can only
access the private section if you have been given permission.

## Using Datasets

<div></div>

For an example on how you can use these datasets in Julia, see below:
```julia
julia> using PyPlot, Seismic
julia> download("http://seismic.physics.ualberta.ca/data/gom_cdp_nmo.su","gom_cdp_nmo.su");
julia> SegyToSeis("gom_cdp_nmo.su","gom_cdp_nmo",format="su",input_type="ieee",swap_bytes=true)
julia> d,h,ext=SeisRead("gom_cdp_nmo");
julia> SeisPlot(d,ext)
```
From a terminal, you can now check the content of `gom_cdp_nmo`.
```sh
msacchi@macbook:~$ more gom_cdp_nmo
```
???+ info "Output"
    ```
            n1=1751
            n2=92
            n3=1
            n4=1
            n5=1
            o1=0.0
            o2=1.0
            o3=0.0
            o4=0.0
            o5=0.0
            d1=0.004
            d2=1.0
            d3=1.0
            d4=1.0
            d5=1.0
            label1="Time"
            label2="Trace Number"
            label3=""
            label4=""
            label5=""
            unit1="s"
            unit2="index"
            unit3=""
            unit4=""
            unit5=""
            title=""
            data_format="native_float"
            esize=4
            in="/Users/msacchi/gom_cdp_nmo@data@"
            headers="/Users/msacchi/gom_cdp_nmo@headers@"
    ```
The binary data is in `gom_cdp_nmo@data@` and the headers are in `gom_cdp_nmo@headers@`.

## Marmousi P-wave Velocity
```julia
julia> using PyPlot, Seismic
julia> download("http://seismic.physics.ualberta.ca/data/marmvel.bin","marmvel.bin");
julia> n1=751;n2=2301; 
julia> dx =4; dz = 4;
julia> f=open("marmvel.bin");
julia> v = read(f, Float32,n1*n2);
julia> SeisPlot(reshape(v,n1,n2),dx=dx,dy=dz)
```

