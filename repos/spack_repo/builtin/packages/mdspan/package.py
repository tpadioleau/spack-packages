# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mdspan(CMakePackage):
    """Extension of std::span to enable multidimensional arrays"""

    homepage = "https://github.com/kokkos/mdspan/tree/stable"
    url = "https://github.com/kokkos/mdspan/releases/download/5.3.0/mdspan-5.3.0.tar.gz"
    git = "https://github.com/kokkos/mdspan.git"

    maintainers("tpadioleau", "nmm0")

    version("stable", branch="stable")
    version("5.3.0", sha256="0d034497e6171c931aabdefa6c50156b95b4a8295c0716f4f42eaaace9abbb6d")

    variant(
        "cxxstd", default="17", values=["14", "17", "20"], multi=False, description="C++ standard"
    )
    variant(
        "stdheaders",
        default=False,
        when="@stable",
        description="Whether to install headers to emulate standard library headers and namespace",
    )

    depends_on("cxx", type="build")

    depends_on("googletest@1.14:1", type="test")

    def cmake_args(self):
        args = [
            self.define("MDSPAN_ENABLE_BENCHMARKS", False),
            self.define("MDSPAN_ENABLE_EXAMPLES", False),
            self.define("MDSPAN_ENABLE_TESTS", self.run_tests),
            self.define("MDSPAN_GENERATE_STD_NAMESPACE_TARGETS", False),
            self.define("MDSPAN_USE_SYSTEM_GTEST", self.run_tests),
            self.define_from_variant("MDSPAN_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("MDSPAN_INSTALL_STDMODE_HEADERS", "stdheaders"),
        ]

        return args
