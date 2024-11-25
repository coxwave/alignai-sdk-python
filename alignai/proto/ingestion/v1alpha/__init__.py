import google.protobuf.runtime_version as _runtime_version

def bypass_runtime_version(*args, **kwargs):
    pass

_runtime_version.ValidateProtobufRuntimeVersion = bypass_runtime_version