import pytest
from graphmaker.resources import (BlockAssignmentFile, CensusShapefileResource,
                                  VTDShapefile, ZippedCensusResource)


def test_shapefiles_implement_path():
    resource = VTDShapefile('26')
    assert resource.path()

    resource = BlockAssignmentFile('26')
    assert resource.path()


def test_census_shapefile_resource_raises_when_file_stem_not_implemented():
    resource = CensusShapefileResource('26')

    with pytest.raises(NotImplementedError):
        resource.path()

    with pytest.raises(NotImplementedError):
        resource.file_stem()


def test_they_all_implement_target_folder():
    resource = ZippedCensusResource('26')
    assert resource.target_folder()

    resource = VTDShapefile('26')
    assert resource.target_folder()

    resource = CensusShapefileResource('26')
    assert resource.target_folder()

    resource = BlockAssignmentFile('26')
    assert resource.target_folder()
