import cv2

print(cv2.getBuildInformation())
# 
# General configuration for OpenCV 4.0.1 =====================================
#   Version control:               unknown
# 
#   Extra modules:
#     Location (extra):            /tmp/opencv-20190105-31032-o160to/opencv-4.0.1/opencv_contrib/modules
#     Version control (extra):     unknown
# 
#   Platform:
#     Timestamp:                   2019-01-05T01:41:15Z
#     Host:                        Darwin 18.2.0 x86_64
#     CMake:                       3.13.2
#     CMake generator:             Unix Makefiles
#     CMake build tool:            /usr/local/Homebrew/Library/Homebrew/shims/mac/super/gmake
#     Configuration:               Release
# 
#   CPU/HW features:
#     Baseline:                    SSE SSE2 SSE3 SSSE3 SSE4_1 POPCNT SSE4_2
#       requested:                 DETECT
#       disabled:                  SSE4_1 SSE4_2 AVX AVX2
#     Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
#       requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
#       SSE4_1 (0 files):          + 
#       SSE4_2 (0 files):          + 
#       FP16 (0 files):            + FP16 AVX
#       AVX (4 files):             + AVX
#       AVX2 (11 files):           + FP16 FMA3 AVX AVX2
#       AVX512_SKX (1 files):      + FP16 FMA3 AVX AVX2 AVX_512F AVX512_SKX
# 
#   C/C++:
#     Built as dynamic libs?:      YES
#     C++ Compiler:                /usr/local/Homebrew/Library/Homebrew/shims/mac/super/clang++  (ver 10.0.0.10001145)
#     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -fvisibility=hidden -fvisibility-inlines-hidden -DNDEBUG  -DNDEBUG
#     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
#     C Compiler:                  /usr/local/Homebrew/Library/Homebrew/shims/mac/super/clang
#     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -fvisibility=hidden -fvisibility-inlines-hidden -DNDEBUG  -DNDEBUG
#     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
#     Linker flags (Release):      
#     Linker flags (Debug):        
#     ccache:                      NO
#     Precompiled headers:         NO
#     Extra dependencies:
#     3rdparty dependencies:
# 
#   OpenCV modules:
#     To be built:                 aruco bgsegm bioinspired calib3d ccalib core datasets dnn dnn_objdetect dpm face features2d flann fuzzy gapi hfs highgui img_hash imgcodecs imgproc java_bindings_generator line_descriptor ml objdetect optflow phase_unwrapping photo plot python2 python3 python_bindings_generator reg rgbd saliency shape stereo stitching structured_light superres surface_matching tracking video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
#     Disabled:                    text world
#     Disabled by dependency:      -
#     Unavailable:                 cnn_3dobj cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv freetype hdf java js matlab ovis sfm ts viz
#     Applications:                apps
#     Documentation:               NO
#     Non-free algorithms:         YES
# 
#   GUI: 
#     Cocoa:                       YES
# 
#   Media I/O: 
#     ZLib:                        /usr/lib/libz.dylib (ver 1.2.11)
#     JPEG:                        build-libjpeg-turbo (ver 1.5.3-62)
#     WEBP:                        build (ver encoder: 0x020e)
#     PNG:                         /usr/local/lib/libpng.dylib (ver 1.6.36)
#     TIFF:                        /usr/local/lib/libtiff.dylib (ver 42 / 4.0.10)
#     OpenEXR:                     /usr/local/lib/libImath.dylib /usr/local/lib/libIlmImf.dylib /usr/local/lib/libIex.dylib /usr/local/lib/libHalf.dylib /usr/local/lib/libIlmThread.dylib (ver 2.2.0)
#     HDR:                         YES
#     SUNRASTER:                   YES
#     PXM:                         YES
#     PFM:                         YES
# 
#   Video I/O:
#     FFMPEG:                      YES
#       avcodec:                   YES (ver 58.35.100)
#       avformat:                  YES (ver 58.20.100)
#       avutil:                    YES (ver 56.22.100)
#       swscale:                   YES (ver 5.3.100)
#       avresample:                YES (ver 4.0.0)
#     AVFoundation:                YES
# 
#   Parallel framework:            TBB (ver 2019.0 interface 11003)
# 
#   Trace:                         YES (with Intel ITT)
# 
#   Other third-party libraries:
#     Intel IPP:                   2019.0.0 Gold [2019.0.0]
#            at:                   /tmp/opencv-20190105-31032-o160to/opencv-4.0.1/build/3rdparty/ippicv/ippicv_mac/icv
#     Intel IPP IW:                sources (2019.0.0)
#               at:                /tmp/opencv-20190105-31032-o160to/opencv-4.0.1/build/3rdparty/ippicv/ippicv_mac/iw
#     Lapack:                      YES (/usr/local/opt/openblas/lib/libopenblas.dylib /usr/local/opt/openblas/lib/libopenblas.dylib)
#     Eigen:                       YES (ver 3.3.7)
#     Custom HAL:                  NO
#     Protobuf:                    build (3.5.1)
# 
#   OpenCL:                        YES (no extra features)
#     Include path:                NO
#     Link libraries:              -framework OpenCL
# 
#   Python 2:
#     Interpreter:                 /usr/local/opt/python@2/bin/python (ver 2.7.15)
#     Libraries:                   /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib (ver 2.7.15)
#     numpy:                       /usr/local/lib/python2.7/site-packages/numpy/core/include (ver 1.15.4)
#     install path:                lib/python2.7/site-packages/cv2/python-2.7
# 
#   Python 3:
#     Interpreter:                 /usr/local/opt/python/bin/python3 (ver 3.7.2)
#     Libraries:                   /usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/lib/python3.7/config-3.7m-darwin/libpython3.7.dylib (ver 3.7.2)
#     numpy:                       /usr/local/lib/python3.7/site-packages/numpy/core/include (ver 1.15.4)
#     install path:                lib/python3.7/site-packages/cv2/python-3.7
# 
#   Python (for build):            /usr/local/opt/python@2/bin/python
# 
#   Java:                          
#     ant:                         NO
#     JNI:                         /Library/Java/JavaVirtualMachines/openjdk-11.0.1.jdk/Contents/Home/include /Library/Java/JavaVirtualMachines/openjdk-11.0.1.jdk/Contents/Home/include/darwin /Library/Java/JavaVirtualMachines/openjdk-11.0.1.jdk/Contents/Home/include
#     Java wrappers:               NO
#     Java tests:                  NO
# 
#   Install to:                    /usr/local/Cellar/opencv/4.0.1
# -----------------------------------------------------------------
# 
# 

print(type(cv2.getBuildInformation()))
# <class 'str'>
