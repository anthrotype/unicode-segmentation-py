from setuptools import setup


def build_native(spec):
    build = spec.add_external_build(
        cmd=["cargo", "build", "--release"], path="./src/rust"
    )

    spec.add_cffi_module(
        module_path="unicode_segmentation._unicode_segmentation",
        dylib=lambda: build.find_dylib(
            "unicode_segmentation_cffi", in_path="target/release"
        ),
        header_filename=lambda: build.find_header(
            "unicode_segmentation_cffi.h", in_path="target"
        ),
        rtld_flags=["NOW", "NODELETE"],
    )


setup(
    name="unicode_segmentation",
    version="0.0.1",
    packages=["unicode_segmentation"],
    package_dir={"": "src/python"},
    zip_safe=False,
    platforms="any",
    setup_requires=["milksnake"],
    install_requires=["milksnake"],
    milksnake_tasks=[build_native],
)
