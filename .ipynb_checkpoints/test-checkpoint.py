try:
    import ansys.fluent.core as pyfluent
    flglobals = pyfluent.setup_for_fluent(product_version="23.2.0", mode="meshing", version="3d", precision="double", processor_count=1)
    globals().update(flglobals)
except Exception:
    pass

workflow.InitializeWorkflow(WorkflowType=r'Watertight Geometry')
meshing.GlobalSettings.LengthUnit.set_state(r'mm')
meshing.GlobalSettings.AreaUnit.set_state(r'mm^2')
meshing.GlobalSettings.VolumeUnit.set_state(r'mm^3')
workflow.TaskObject['Import Geometry'].Arguments.set_state({r'FileName': r'C:/Users/hieup/Documents/my-repo-gihub/ansys-pyfluent-tutorial/PyF_L3_WF/Workshop_files/Input_files/Static Mixer geometry.dsco',})
workflow.TaskObject['Import Geometry'].Execute()
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate()
workflow.TaskObject['Generate the Surface Mesh'].Execute()
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=False)
workflow.TaskObject['Describe Geometry'].Arguments.set_state({f'SetupType': r'The geometry consists of only fluid regions with no void',})
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=True)
workflow.TaskObject['Describe Geometry'].Execute()
workflow.TaskObject['Update Boundaries'].Execute()
workflow.TaskObject['Update Regions'].Execute()
workflow.TaskObject['Add Boundary Layers'].Arguments.set_state({r'LocakPrismPreferences': {r'Continuous': r'Stair Step',} })
workflow.TaskObject['Add Boundary Layers'].AddChildAndUpdate()
workflow.TaskObject['Generate the Volume Mesh'].Execute()
meshing.execute_tui(r'''/switch-to-solution-mode yes''')
solver.execute_tui(r'''(newline)''')
solver.setup.models.energy = {"enabled" : True}
solver.tui.define.materials.copy('fluid', 'water-liquid')
solver.setup.cell_zone_conditions.fluid['fluid'] = {"reference_frame_axis_direction" : [1, 0, 1]}
solver.setup.boundary_conditions.velocity_inlet['velocity-inlet-1'] = {"vmag" : 1.}
solver.setup.boundary_conditions.velocity_inlet['velocity-inlet-1'] = {"vmag" : 1.}
solver.setup.boundary_conditions.velocity_inlet['velocity-inlet-2'] = {"vmag" : 1.}
solver.setup.boundary_conditions.velocity_inlet['velocity-inlet-2'] = {"vmag" : 1.}
solver.solution.initialization.hybrid_initialize()
solver.solution.run_calculation.iterate(iter_count = 20)
solver.exit()
