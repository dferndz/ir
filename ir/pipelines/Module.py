class Module:
    def forward(self, *args, **kwargs):
        raise NotImplementedError("Implement forward() in derived classes!")

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
