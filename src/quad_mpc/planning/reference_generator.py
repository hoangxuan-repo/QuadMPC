"""Generate desired base pose and velocity references."""


class ReferenceGenerator:
    def get_reference(self, time):
        raise NotImplementedError
