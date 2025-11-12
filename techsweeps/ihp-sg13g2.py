from pygmid.sweep import SweepConfig
from typing import List, Tuple, Optional, Union


class IHPConfig(SweepConfig):
    """ IHP Configuration class for sweep simulations using ngspice. """
    def __post_init__(self):
        super().__post_init__()
    
    def write_params(self, length: Optional[Union[float, str]]=None, sb: Optional[Union[float, str]]=None, **kwargs):
        return super().write_params(length, sb, **kwargs)
    
    def generate_outvars(self, n: List=[], p: List=[], n_noise: List=[], p_noise: List=[]) -> Tuple[List, List, List, List]:
        """ Generate the mapping of output variables from the simulation to the lookup table. 
        
        outvars: `['ID','VT','IGD','IGS','GM','GMB','GDS','CGG','CGS','CSG','CGD','CDG','CGB','CDD','CSS']`
        outvars_noise: `['STH','SFL']`

        """
        n.append( ['n.xm1.n:ids','A',   	[1,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:vth','V',   	[0,    1,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:igd','A',   	[0,    0,   1,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:igs','A',   	[0,    0,   0,    1,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:gm','S',    	[0,    0,   0,    0,    1,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:gmb','S',  	    [0,    0,   0,    0,    0,   1,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:gds','S',   	[0,    0,   0,    0,    0,   0,    1,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:cgg','F',   	[0,    0,   0,    0,    0,   0,    0,    1,    0,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:cgdol','F',   	[0,    0,   0,    0,    0,   0,    0,    1,    0,    0,    1,    0,    0,    1,    0  ]])
        n.append( ['n.xm1.n:cgsol','F',   	[0,    0,   0,    0,    0,   0,    0,    1,    1,    0,    0,    0,    0,    0,    1  ]])
        n.append( ['n.xm1.n:cgs','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    1,    0,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:cgd','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    1,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:cgb','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    1,    0,    0  ]])
        n.append( ['n.xm1.n:cdd','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    1,    0  ]])
        n.append( ['n.xm1.n:cdg','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    1,    0,    0,    0  ]])
        n.append( ['n.xm1.n:css','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    1  ]])
        n.append( ['n.xm1.n:csg','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    1,    0,    0,    0,    0,    0  ]])
        n.append( ['n.xm1.n:cjd','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    1,    0  ]])
        n.append( ['n.xm1.n:cjs','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    1  ]])

        p.append( ['n.xm2.n:ids','A',   	[1,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:vth','V',   	[0,    1,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:igd','A',   	[0,    0,   1,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:igs','A',   	[0,    0,   0,    1,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:gm','S',    	[0,    0,   0,    0,    1,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:gmb','S',  	    [0,    0,   0,    0,    0,   1,    0,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:gds','S',   	[0,    0,   0,    0,    0,   0,    1,    0,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:cgg','F',   	[0,    0,   0,    0,    0,   0,    0,    1,    0,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:cgdol','F',   	[0,    0,   0,    0,    0,   0,    0,    1,    0,    0,    1,    0,    0,    1,    0  ]])
        p.append( ['n.xm2.n:cgsol','F',   	[0,    0,   0,    0,    0,   0,    0,    1,    1,    0,    0,    0,    0,    0,    1  ]])
        p.append( ['n.xm2.n:cgs','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    1,    0,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:cgd','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    1,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:cgb','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    1,    0,    0  ]])
        p.append( ['n.xm2.n:cdd','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    1,    0  ]])
        p.append( ['n.xm2.n:cdg','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    1,    0,    0,    0  ]])
        p.append( ['n.xm2.n:css','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    1  ]])
        p.append( ['n.xm2.n:csg','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    1,    0,    0,    0,    0,    0  ]])
        p.append( ['n.xm2.n:cjd','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    1,    0  ]])
        p.append( ['n.xm2.n:cjs','F',   	[0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,    0,    0,    0,    1  ]])
        
        n_noise.append(['n.xm1.n:sid', ''])
        n_noise.append(['n.xm1.n:sfl', ''])
        
        p_noise.append(['n.xm2.n:sid', ''])
        p_noise.append(['n.xm2.n:sfl', ''])
        return (n, p, n_noise, p_noise)
