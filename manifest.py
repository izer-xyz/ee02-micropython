c_module("Inkplate-micropython/firmware/usermods/inkplate")

freeze("Inkplate-micropython/shared/drivers")
freeze("Inkplate-micropython/shared/mixins")
module("gfx_standard_font_01.py", base_path="Inkplate-micropython/shared")

freeze("src")
