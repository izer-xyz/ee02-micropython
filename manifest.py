c_module("Inkplate-micropython/firmware/usermods/inkplate")
module("inkplate13_spectra.py", base_path="Inkplate-micropython/boards/inkplate13spectra")

freeze("Inkplate-micropython/shared/drivers")
freeze("Inkplate-micropython/shared/mixins")

module("gfx_standard_font_01.py", base_path="Inkplate-micropython/shared")
