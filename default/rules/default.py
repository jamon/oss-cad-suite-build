from src.base import Target

Target(
    name = 'default',
    release_name = 'oss-cad-suite',
    top_package = True,
    dependencies = [
        'yosys',
        'ghdl',
        'ghdl-yosys-plugin',
        'nextpnr-generic',
        'nextpnr-ice40',
        'nextpnr-ecp5',
        'nextpnr-machxo2',
        'nextpnr-nexus',
        'nextpnr-gowin',
        'icestorm',
        'prjtrellis',
        'prjoxide',
        'apicula',
        'dfu-util',
        'ecpprog',
        'openfpgaloader',
        'aiger',
        'avy',
        'bitwuzla',
        'boolector',
        'cvc4',
        'cvc5',
        'yices',
        'suprove',
        'pono',
        'z3',
        'mcy',
        'eqy',
        'sby',
        'sby-gui',
        'gtkwave',
        'verilator',
        'iverilog',
        'ecpdap',
        'fujprog',
        'iceprogduino',
        'python-programmers',
        'openocd',
        'icesprog',
        'utils',
        'pyhdl',
        'cocotb',
        'surelog',
        'surelog-data',
        'surelog-plugin',
    ],
    branding = 'OSS CAD Suite',
    readme = 'README',
    resources = [ 'system-resources' ],
)

Target(
    name = 'default-formal',
    release_name = 'oss-cad-suite-formal',
    top_package = True,
    dependencies = [
        'yosys',
        'aiger',
        'avy',
        'bitwuzla',
        'boolector',
        'cvc4',
        'cvc5',
        'yices',
        'suprove',
        'pono',
        'z3',
        'mcy',
        'eqy',
        'sby',
        'sby-gui',
        'gtkwave',
    ],
    branding ='OSS CAD Formal',
    readme = 'README',
    resources = [ 'system-resources' ],
)

Target(
    name = 'yosyshq-ci',
    release_name = 'oss-cad-suite-ci',
    top_package = True,
    dependencies = [
        'aiger',
        'avy',
        'bitwuzla',
        'boolector',
        'cvc4',
        'cvc5',
        'yices',
        'suprove',
        'pono',
        'z3',
        'mcy',
        'eqy',
        'sby',
        'gtkwave',
        'iverilog',
    ],
    branding ='OSS CAD Suite',
    readme = 'README',
    resources = [ 'system-resources' ],
)
