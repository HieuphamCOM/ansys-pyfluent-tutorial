try:
    import ansys.fluent.core as pyfluent
    flglobals = pyfluent.setup_for_fluent(product_version="23.2.0", mode="meshing", version="3d", precision="double", processor_count=1)
    globals().update(flglobals)
except Exception:
    pass

workflow.InitializeWorkflow(WorkflowType=r'Watertight Geometry')
