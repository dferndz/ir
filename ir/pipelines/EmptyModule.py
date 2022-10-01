from .Module import Module


class EmptyModule(Module):
    def forward(self, x):
        return x
