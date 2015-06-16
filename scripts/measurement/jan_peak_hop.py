#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 30
  detector: H1
  mass: 39.59
default_fits: nominal
equilibration:
  eqtime: 15
  inlet: C
  inlet_delay: 3
  outlet: E
  use_extraction_eqtime: false
multicollect:
  counts: 50
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  isotope: Ar40
  detectors:
   - H1
   - AX
   - CDD
peakhop:
  hops_name: hop
  use_peak_hop: true
  ncycles: 12
 '''

ACTIVE_DETECTORS=('H2','H1','AX','L1','L2','CDD')


def main():
    info('peak hop measurement script')

    activate_detectors(*ACTIVE_DETECTORS)

    position_magnet('Ar40', detector='H1')

    hops=load_hops('hops/{}.txt'.format(mx.peakhop.hops_name))
    define_hops(hops)

    if mx.equilibration.use_extraction_eqtime:
        e = ex.eqtime
    else:
        e = mx.equilibration.eqtime

    equilibrate(eqtime=e, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet)

    #equilibrate returns immediately after the inlet opens
    set_time_zero()

    sniff(e)
    #set default regression
    set_fits()
    set_baseline_fits()

    peak_hop(ncycles=mx.peakhop.ncycles, hops=hops)


    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)

    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    info('finished measure script')
