from conans import ConanFile

class HelloStatlibConan(ConanFile):
    name = "hello_statlib"
    version = "1.0.0"
    description = "Hello static library https://github.com/Twoflower2/conan_cdt/blob/master/README.md"
    url = "https://github.com/Twoflower2/conan_cdt"
    license = "BSD"
    author = "Twoflower2"
    settings = "os", "compiler", "build_type"
    exports_sources = "inc*", "src*", "workspace*"
    generators = "txt"

    def build(self):
        os.makedirs("bin")
        
        # ***************************************************************************************
        # Calls eclipse with 4 arguments as defined per list below:
        #    argument list = WORK_SPACE value as 1st argument
        #                    PROJECT_DIR value as 2nd argument
        #                    PROJECT_NAME value as 3rd argument
        #                    BUILD_TYPE option as 4th argument as defined in project
        # ***************************************************************************************
        #
        # (In order to see what happens: add option -debug to eclipse cmd)
        #
        # Using a release of Eclipse 3.5 + CDT 6, you can import, build and clean-build projects and the workspace using the following options sent to Eclipse at the command line:
        #
        # eclipse -nosplash
        #         -application org.eclipse.cdt.managedbuilder.core.headlessbuild
        #         -data {[uri:/]/path/to/workspace}
        #         -import {[uri:/]/path/to/project}
        #         -build {project_name | all}
        #         -cleanBuild {projec_name | all}
        #         %ECLIPSE_EXTENDED_ARGS%
        #
        # The '-application' switch instructs Eclipse to run the CDT headless builder rather than starting the workbench. The other switches can be used individually or together.
        # This means you can checkout a project using a shell script of your own, '-import' it into a workspace, and '-build' it using the Managedbuilder's headless builder.
        #
        # Use the '-data' switch to specify the workspace to use, which can be an empty temporary directory, see the runtime documentation for other switches supported by the platform runtime
        #      http://help.eclipse.org/indigo/index.jsp?topic=/org.eclipse.platform.doc.isv/reference/misc/runtime-options.html
        #
        # ***************************************************************************************

        WORK_SPACE = "workspace"
        PROJECT_NAME = "hello_statlib" #Just set here as explicit example only. This is important as var for build per project_name, because we have up to 42 project_name 's each having a .cproject file
        PROJECT_DIR = "workspace/" + PROJECT_NAME
        self.settings.build_type = "Debug" #Just set here as explicit example only
        BUILD_TYPE = str(self.settings.build_type)
        
        cmd = "eclipse -nosplash -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + WORK_SPACE + " -import " + PROJECT_DIR + " -cleanBuild " + PROJECT_NAME + "/" + BUILD_TYPE
        print("\nBuilding with command line cmd:\n" + cmd)
        self.run(cmd)
        print("\nBuild Successful")

    def package_info(self):
        self.cpp_info.includedirs= ["inc"]
        self.cpp_info.libdirs = ["bin"]

    def package(self):
        self.copy(pattern="*.a", dst="bin", src="bin")
        self.copy(pattern="*.h", dst="inc", src="inc")

    # def env_info(self):
    #     self.env_info.path.append("C:\\Program Files\\Java.x\\jdk1.7.0_25\\bin")  # Append "ANOTHER VALUE" to the path variable
    #     self.env_info.path.append("C:\\Program Files\\Java.x\\jdk1.7.0_25\\bin")  # Append "ANOTHER VALUE" to the path variable
