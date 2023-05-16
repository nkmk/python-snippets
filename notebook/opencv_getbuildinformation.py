import cv2

print(cv2.getBuildInformation())
# 
# General configuration for OpenCV 4.7.0 =====================================
#   Version control:               unknown
# 
#   Extra modules:
#     Location (extra):            /tmp/opencv-20230423-16173-kbjcfg/opencv-4.7.0/opencv_contrib/modules
#     Version control (extra):     unknown
# 
#   Platform:
#     Timestamp:                   2022-12-28T14:31:52Z
#     Host:                        Darwin 21.6.0 arm64
#     CMake:                       3.26.3
#     CMake generator:             Unix Makefiles
#     CMake build tool:            gmake
#     Configuration:               Release
# 
#   CPU/HW features:
#     Baseline:                    NEON FP16
# 
#   C/C++:
#     Built as dynamic libs?:      YES
#     C++ standard:                11
#     C++ Compiler:                clang++  (ver 14.0.0.14000029)
#     C++ flags (Release):         -fsigned-char -W -Wall -Wreturn-type -Wnon-virtual-dtor -Waddress -Wsequence-point -Wformat -Wformat-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
#     C++ flags (Debug):           -fsigned-char -W -Wall -Wreturn-type -Wnon-virtual-dtor -Waddress -Wsequence-point -Wformat -Wformat-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
#     C Compiler:                  clang
#     C flags (Release):           -fsigned-char -W -Wall -Wreturn-type -Wnon-virtual-dtor -Waddress -Wsequence-point -Wformat -Wformat-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
#     C flags (Debug):             -fsigned-char -W -Wall -Wreturn-type -Wnon-virtual-dtor -Waddress -Wsequence-point -Wformat -Wformat-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
#     Linker flags (Release):      -Wl,-dead_strip  
#     Linker flags (Debug):        -Wl,-dead_strip  
#     ccache:                      NO
#     Precompiled headers:         NO
#     Extra dependencies:
#     3rdparty dependencies:
# 
#   OpenCV modules:
#     To be built:                 alphamat aruco barcode bgsegm bioinspired calib3d ccalib core datasets dnn dnn_objdetect dnn_superres dpm face features2d flann freetype fuzzy gapi hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python3 quality rapid reg rgbd saliency sfm shape stereo stitching structured_light superres surface_matching text tracking video videoio videostab viz wechat_qrcode xfeatures2d ximgproc xobjdetect xphoto
#     Disabled:                    hdf world
#     Disabled by dependency:      -
#     Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv java julia matlab ovis python2 ts
#     Applications:                apps
#     Documentation:               NO
#     Non-free algorithms:         YES
# 
#   GUI:                           COCOA
#     Cocoa:                       YES
#     VTK support:                 YES (ver 9.2.6)
# 
#   Media I/O: 
#     ZLib:                        /Library/Developer/CommandLineTools/SDKs/MacOSX12.sdk/usr/lib/libz.tbd (ver 1.2.11)
#     JPEG:                        /opt/homebrew/lib/libjpeg.dylib (ver 80)
#     WEBP:                        /opt/homebrew/lib/libwebp.dylib (ver encoder: 0x020f)
#     PNG:                         /opt/homebrew/lib/libpng.dylib (ver 1.6.39)
#     TIFF:                        /opt/homebrew/lib/libtiff.dylib (ver 42 / 4.5.0)
#     JPEG 2000:                   OpenJPEG (ver 2.5.0)
#     OpenEXR:                     OpenEXR::OpenEXR (ver 3.1.7)
#     HDR:                         YES
#     SUNRASTER:                   YES
#     PXM:                         YES
#     PFM:                         YES
# 
#   Video I/O:
#     FFMPEG:                      YES
#       avcodec:                   YES (60.3.100)
#       avformat:                  YES (60.3.100)
#       avutil:                    YES (58.2.100)
#       swscale:                   YES (7.1.100)
#       avresample:                NO
#     AVFoundation:                YES
# 
#   Parallel framework:            TBB (ver 2021.9 interface 12090)
# 
#   Trace:                         YES (with Intel ITT)
# 
#   Other third-party libraries:
#     Lapack:                      YES (/opt/homebrew/opt/openblas/lib/libopenblas.dylib)
#     Eigen:                       YES (ver 3.4.0)
#     Custom HAL:                  YES (carotene (ver 0.0.1))
#     Protobuf:                    /opt/homebrew/lib/libprotobuf.dylib (3.21.12)
# 
#   OpenCL:                        YES (no extra features)
#     Include path:                NO
#     Link libraries:              -framework OpenCL
# 
#   Python 3:
#     Interpreter:                 /opt/homebrew/opt/python@3.11/bin/python3.11 (ver 3.11.3)
#     Libraries:                   /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib (ver 3.11.3)
#     numpy:                       /opt/homebrew/lib/python3.11/site-packages/numpy/core/include (ver 1.24.3)
#     install path:                lib/python3.11/site-packages/cv2/python-3.11
# 
#   Python (for build):            /opt/homebrew/opt/python@3.11/bin/python3.11
# 
#   Java:                          
#     ant:                         NO
#     JNI:                         NO
#     Java wrappers:               NO
#     Java tests:                  NO
# 
#   Install to:                    /opt/homebrew/Cellar/opencv/4.7.0_4
# -----------------------------------------------------------------
# 
# 

print(type(cv2.getBuildInformation()))
# <class 'str'>
