import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class nlohmannjson(mama.BuildTarget):

    def dependencies(self):
        self.nothing_to_build()

    def configure(self):
        self.add_cmake_options('JSON_BuildTests=OFF', 'JSON_Install=OFF', 'JSON_MultipleHeaders=OFF')

    ## optional: customize package exports if repository doesn't have `include` or `src`
    ##           default include and lib export works for most common static libs
    def package(self):
        self.export_include('single_include')

