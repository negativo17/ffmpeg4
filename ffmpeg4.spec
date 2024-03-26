%global _lto_cflags %{nil}

%global avcodec_soversion 58
%global avdevice_soversion 58
%global avfilter_soversion 7
%global avformat_soversion 58
%global avresample_soversion 4
%global avutil_soversion 56
%global postproc_soversion 55
%global swresample_soversion 3
%global swscale_soversion 5

# NVCC + Glibc 2.38 (f39+) on aarch64 currently broken:
%ifarch x86_64
%bcond_without cuda
%else
%bcond_with cuda
%endif

%ifarch aarch64
%if 0%{?fedora} == 38 || 0%{?rhel} >= 7
%bcond_without cuda
%else
%bcond_with cuda
%endif
%endif

Summary:        A complete solution to record, convert and stream audio and video
Name:           ffmpeg4
Version:        4.4.4
Release:        4%{?dist}
License:        LGPLv3+
URL:            http://%{name}.org/
Epoch:          1

Source0:        http://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz

Patch0:         %{name}-cuda11.patch
# https://github.com/OpenVisualCloud/SVT-VP9/tree/master/ffmpeg_plugin
Patch1:         %{name}-svt-vp9.patch
# https://github.com/OpenVisualCloud/SVT-HEVC/tree/master/ffmpeg_plugin
Patch2:         %{name}-svt-hevc.patch
# https://framagit.org/tytan652/ffmpeg-ndi-patch
Patch3:         %{name}-ndi.patch

BuildRequires:  AMF-devel
BuildRequires:  bzip2-devel
BuildRequires:  codec2-devel
BuildRequires:  decklink-devel >= 11.5
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  gmp-devel
BuildRequires:  gsm-devel
BuildRequires:  ilbc-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  ladspa-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  libdav1d-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libndi-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  libxml2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  nasm
BuildRequires:  ocl-icd-devel
BuildRequires:  openal-soft-devel
BuildRequires:  opencl-headers
BuildRequires:  opencore-amr-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  snappy-devel
BuildRequires:  soxr-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  xvidcore-devel
BuildRequires:  xz-devel
BuildRequires:  zvbi-devel >= 0.2.28

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom) >= 1.0.0
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(davs2) >= 1.5.115
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(kvazaar) >= 0.8.1
#BuildRequires:  pkgconfig(lensfun) >= 0.3.95
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librabbitmq) >= 0.7.1
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(uavs3d) >= 1.1.41
BuildRequires:  pkgconfig(vidstab) >= 0.98
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(xavs2) >= 1.2.77
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(x264) >= 0.118
BuildRequires:  pkgconfig(x265) >= 0.68
BuildRequires:  pkgconfig(zimg) >= 2.7.0
BuildRequires:  pkgconfig(zlib)

%if 0%{?fedora}
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
%if 0%{?fedora} < 39
BuildRequires:  pkgconfig(pocketsphinx)
%endif
BuildRequires:  pkgconfig(rav1e) >= 0.4.0
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libzmq) >= 4.2.1
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(vapoursynth-script) >= 42
BuildRequires:  pkgconfig(vulkan) >= 1.1.97
%endif

%if 0%{?fedora} || 0%{?rhel} == 7   || 0%{?rhel} == 8
BuildRequires:  frei0r-devel
%endif

%ifarch x86_64 aarch64
# Nvidia CUVID support and Performance Primitives based code
BuildRequires:  cuda-cudart-devel
BuildRequires:  cuda-nvcc
BuildRequires:  libnpp-devel
BuildRequires:  pkgconfig(ffnvcodec) >= 8.1.24.2
%endif

%ifarch x86_64
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libvmaf) >= 1.5.2
BuildRequires:  pkgconfig(SvtAv1Enc)
BuildRequires:  pkgconfig(SvtHevcEnc) >= 1.5.1
BuildRequires:  pkgconfig(SvtVp9Enc)
%endif

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package     -n libavcodec58
Summary:        FFmpeg codec library

%description -n libavcodec58
The libavcodec library provides a generic encoding/decoding framework and
contains multiple decoders and encoders for audio, video and subtitle streams,
and several bitstream filters.

%package     -n libavcodec58-devel
Summary:        Development files for FFmpeg's codec library
Requires:       libavcodec58%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libavcodec58-devel
The libavcodec library provides a generic encoding/decoding framework and
contains multiple decoders and encoders for audio, video and subtitle streams,
and several bitstream filters.
 
This subpackage contains the headers for FFmpeg libavcodec.

%package     -n libavdevice58
Summary:        FFMpeg devices muxing/demuxing library

%description -n libavdevice58
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.

%package     -n libavdevice58-devel
Summary:        Development files for FFMpeg devices muxing/demuxing library
Requires:       libavcodec58-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavdevice58%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavfilter7-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavformat58-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libavdevice58-devel
This subpackage contains the headers for FFmpeg libavdevice.

%package     -n libavfilter7
Summary:        FFmpeg audio and video filtering library
Requires:       libavcodec58%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavformat58%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavutil56%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libpostproc55%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswresample3%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswscale5%{?_isa} = %{?epoch}:%{version}-%{release}

%description -n libavfilter7
The libavfilter library provides a generic audio/video filtering framework
containing several filters, sources and sinks.

%package     -n libavfilter7-devel
Summary:        Development files for FFmpeg's audio/video filter library
Requires:       libavcodec58-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavfilter7%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavformat58-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libpostproc55-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswresample3-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswscale5-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libavfilter7-devel
This subpackage contains the headers for FFmpeg libavfilter.

%package     -n libavformat58
Summary:        FFmpeg's stream format library

%description -n libavformat58
The libavformat library provides a generic framework for multiplexing and
demultiplexing (muxing and demuxing) audio, video and subtitle streams.
It encompasses multiple muxers and demuxers for multimedia container formats.

%package     -n libavformat58-devel
Summary:        Development files for FFmpeg's stream format library
Requires:       libavcodec58-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavformat58%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswresample3-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libavformat58-devel
This subpackage contains the headers for FFmpeg libavformat.

%package     -n libavresample4
Summary:        FFmpeg's stream format library

%description -n libavresample4
Libavresample (lavr) is a library that handles audio resampling, sample format
conversion and mixing.

%package     -n libavresample4-devel
Summary:        Development files for FFmpeg's stream format library
Requires:       libavresample4%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libavresample4-devel
This subpackage contains the headers for FFmpeg libavresample.

%package     -n libavutil56
Summary:        FFmpeg's utility library

%description -n libavutil56
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

%package     -n libavutil56-devel
Summary:        Development files for FFmpeg's utility library
Requires:       libavutil56%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libavutil56-devel
This subpackage contains the headers for FFmpeg libavutil.

%package     -n libpostproc55
Summary:        FFmpeg post-processing library

%description -n libpostproc55
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

%package     -n libpostproc55-devel
Summary:        Development files for the FFmpeg post-processing library
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libpostproc55%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n libpostproc55-devel
This subpackage contains the headers for FFmpeg libpostproc.

%package     -n libswresample3
Summary:        FFmpeg software resampling library
Requires:       libavutil56%{?_isa} = %{?epoch}:%{version}-%{release}

%description -n libswresample3
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%package     -n libswresample3-devel
Summary:        Development files for the FFmpeg software resampling library
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswresample3%{?_isa} = %{?epoch}:%{version}-%{release}

%description -n libswresample3-devel
This subpackage contains the headers for FFmpeg libswresample.

%package     -n libswscale5
Summary:        FFmpeg image scaling and colorspace/pixel conversion library

%description -n libswscale5
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%package     -n libswscale5-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Requires:       libavutil56-devel%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libswscale5%{?_isa} = %{?epoch}:%{version}-%{release}

%description -n libswscale5-devel
This subpackage contains the headers for FFmpeg libswscale.

%prep
%autosetup -p1 -n ffmpeg-%{version}

# Uncomment to enable debugging while configuring
#sed -i -e 's|#!/bin/sh|#!/bin/sh -x|g' configure

%build
./configure \
    --arch=%{_target_cpu} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --disable-debug \
    --disable-programs \
    --disable-static \
    --disable-stripping \
    --enable-amf \
    --enable-avcodec \
    --enable-avdevice \
    --enable-avfilter \
    --enable-avformat \
    --enable-avresample \
    --enable-alsa \
    --enable-bzlib \
    --enable-chromaprint \
    --enable-decklink \
    --enable-gcrypt \
    --enable-gmp \
    --enable-gpl \
    --enable-gray \
    --enable-iconv \
    --enable-ladspa \
    --enable-libass \
    --enable-libaom \
    --enable-libbluray \
    --enable-libbs2b \
    --enable-libcaca \
    --enable-libcdio \
    --enable-libcodec2 \
    --enable-libdc1394 \
    --enable-libdav1d \
    --enable-libdavs2 \
    --enable-libdrm \
    --enable-libfdk-aac \
    --enable-libfontconfig \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgme \
    --enable-libgsm \
    --enable-libiec61883 \
    --enable-libilbc \
    --enable-libjack \
    --enable-libkvazaar \
    --enable-libmodplug \
    --enable-libmp3lame \
    --enable-libndi_newtek \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopenmpt \
    --enable-libopus \
    --enable-libpulse \
    --enable-librabbitmq \
    --enable-librsvg \
    --enable-librubberband \
    --enable-libsmbclient \
    --enable-libsnappy \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtesseract \
    --enable-libtheora \
    --enable-libtwolame \
    --enable-libuavs3d \
    --enable-libv4l2 \
    --enable-libvidstab \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxavs2 \
    --enable-libxcb \
    --enable-libxcb-shape \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxml2 \
    --enable-libxvid \
    --enable-libzimg \
    --enable-libzvbi \
    --enable-lzma \
    --enable-nonfree \
    --enable-openal \
    --enable-opencl \
    --enable-opengl \
    --enable-openssl \
    --enable-postproc \
    --enable-sdl2 \
    --enable-shared \
    --enable-swresample \
    --enable-swscale \
    --enable-vaapi \
    --enable-version3 \
    --enable-vdpau \
    --enable-xlib \
    --enable-zlib \
    --incdir=%{_includedir} \
    --libdir=%{_libdir} \
    --optflags="%{optflags}" \
    --prefix=%{_prefix} \
    --shlibdir=%{_libdir} \
%if 0%{?fedora}
    --enable-librav1e \
    --enable-lv2 \
%if 0%{?fedora} < 39
    --enable-pocketsphinx \
%endif
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
    --enable-libsrt \
    --enable-libzmq \
    --enable-v4l2-m2m \
    --enable-vapoursynth \
    --enable-vulkan \
%endif
%if 0%{?fedora} || 0%{?rhel} == 7 || 0%{?rhel} == 8
    --enable-frei0r \
%endif
%ifarch x86_64 aarch64
%if %{with cuda}
    --enable-cuda-nvcc \
%endif
    --enable-cuvid \
    --enable-ffnvcodec \
    --enable-libnpp \
    --enable-nvdec \
    --enable-nvenc \
    --extra-cflags="-I%{_includedir}/cuda" \
%endif
%ifarch x86_64
    --enable-libsvtav1 \
    --enable-libsvthevc \
    --enable-libsvtvp9 \
    --enable-libvmaf \
%endif
%ifarch ppc
    --cpu=g3 \
    --enable-pic \
%endif
%ifarch ppc64
    --cpu=g5 \
    --enable-pic \
%endif
%ifarch %{arm}
    --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%endif

%make_build

%install
%make_install
# Let rpmbuild pick up the docs
rm -fr %{buildroot}%{_docdir}/*
rm -fr %{buildroot}%{_datadir}/%{name}/examples

%ldconfig_scriptlets -n libavcodec58
%ldconfig_scriptlets -n libavdevice58
%ldconfig_scriptlets -n libavfilter7
%ldconfig_scriptlets -n libavformat58
%ldconfig_scriptlets -n libavresample4
%ldconfig_scriptlets -n libavutil56
%ldconfig_scriptlets -n libpostproc55
%ldconfig_scriptlets -n libswresample3
%ldconfig_scriptlets -n libswscale5

%files -n libavcodec58
%license COPYING.* LICENSE.md
%{_libdir}/libavcodec.so.%{avcodec_soversion}*

%files -n libavcodec58-devel
%{_includedir}/libavcodec
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/libavcodec.so

%files -n libavdevice58
%license COPYING.* LICENSE.md
%{_libdir}/libavdevice.so.%{avdevice_soversion}*

%files -n libavdevice58-devel
%{_includedir}/libavdevice
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/libavdevice.so

%files -n libavfilter7
%license COPYING.* LICENSE.md
%{_libdir}/libavfilter.so.%{avfilter_soversion}*

%files -n libavfilter7-devel
%{_includedir}/libavfilter
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/libavfilter.so

%files -n libavformat58
%license COPYING.* LICENSE.md
%{_libdir}/libavformat.so.%{avformat_soversion}*

%files -n libavformat58-devel
%{_includedir}/libavformat
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/libavformat.so

%files -n libavutil56
%license COPYING.* LICENSE.md
%{_libdir}/libavutil.so.%{avutil_soversion}*

%files -n libavutil56-devel
%{_includedir}/libavutil
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/libavutil.so

%files -n libavresample4
%license COPYING.* LICENSE.md
%{_libdir}/libavresample.so.%{avresample_soversion}*

%files -n libavresample4-devel
%{_includedir}/libavresample
%{_libdir}/pkgconfig/libavresample.pc
%{_libdir}/libavresample.so

%files -n libpostproc55
%license COPYING.* LICENSE.md
%{_libdir}/libpostproc.so.%{postproc_soversion}*

%files -n libpostproc55-devel
%{_includedir}/libpostproc
%{_libdir}/pkgconfig/libpostproc.pc
%{_libdir}/libpostproc.so

%files -n libswresample3
%license COPYING.* LICENSE.md
%{_libdir}/libswresample.so.%{swresample_soversion}*

%files -n libswresample3-devel
%{_includedir}/libswresample
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/libswresample.so

%files -n libswscale5
%license COPYING.* LICENSE.md
%{_libdir}/libswscale.so.%{swscale_soversion}*

%files -n libswscale5-devel
%{_includedir}/libswscale
%{_libdir}/pkgconfig/libswscale.pc
%{_libdir}/libswscale.so

%changelog
* Tue Mar 26 2024 Simone Caronni <negativo17@gmail.com> - 1:4.4.4-4
- NVCC + Glibc 2.38 on ARM is currently broken.
- Disable glslang.

* Sat Mar 23 2024 Simone Caronni <negativo17@gmail.com> - 1:4.4.4-3
- Enable Nvidia CUDA, performance primitives, encoding/decoding also on aarch64.

* Tue Oct 03 2023 Simone Caronni <negativo17@gmail.com> - 1:4.4.4-2
- Momentarily disable pocketsphinx support for Fedora 39+.

* Tue Jun 13 2023 Simone Caronni <negativo17@gmail.com> - 1:4.4.4-1
- Update to 4.4.4.

* Fri Jun 02 2023 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-7
- Rebuild for updated dependencies.

* Sat Mar 11 2023 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-6
- Rebuild for updated depdendencies.

* Fri Feb 03 2023 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-5
- Rebuild for updated dependencies.

* Thu Jan 05 2023 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-4
- Rebuild for updated dependencies.

* Fri Dec 23 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-3
- Drop librtmp support, use native rtmp.

* Thu Dec 15 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-2
- Rebuild for updated dependencies.

* Sun Nov 20 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.3-1
- Update to 4.4.3.

* Thu Sep 22 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.2-5
- Rebuild for updated dependencies.
- Drop OpenCV support everywhere.

* Tue Jul 05 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.2-4
- Disable frei0r on CentOS/RHEL 9.
- Enable OpenCV on Fedora and CentOS/RHEL 7 and 8.

* Wed Jun 01 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.2-3
- Rebuild for updated dependencies.

* Tue May 24 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.2-2
- Drop XVideo Motion Compensation support.

* Sun Apr 17 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.2-1
- Update to 4.4.2.

* Sun Apr 10 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-8
- Create ffmpeg4 compatibility package.

* Thu Mar 17 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-7
- Split libraries in subpackages like in Fedora 36.

* Wed Mar 16 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-6
- Enable AVS3 decoder for real.

* Wed Mar 16 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-5
- Enable AVS3 decoder.

* Mon Mar 14 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-4
- Enable NDI support also for aarch64.

* Thu Feb 10 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-3
- Enable Advanced Media Framework support (Mesa/PRO AMD encoding).

* Sun Feb 06 2022 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-2
- Stop putting headers under a subfolder.
- Reorganize CUDA build.

* Tue Nov 02 2021 Simone Caronni <negativo17@gmail.com> - 1:4.4.1-1
- Update to 4.4.1.

* Fri Jul 23 2021 Simone Caronni <negativo17@gmail.com> - 1:4.4-1
- Update to 4.4, review libraries and options.
- Update external patches.
- Switch from GnuTLS to OpenSSL.
- Trim changelog.

* Tue Jul 20 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-4
- Rebuild for updated dependencies.

* Sun Jun 20 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-3
- Rebuild for updated dependencies.

* Thu Mar 25 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-2
- Re-enable NDI support.

* Mon Mar 01 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-1
- Update to 4.3.2.

* Sat Dec 05 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-4
- Rebuild for updated dependencies.

* Thu Nov 26 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-3
- Add SVT HEVC, AV1 and VP9 patches.

* Tue Nov 17 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-2
- Rebuild for updated CUDA libraries.

* Tue Aug 25 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-1
- Update to 4.3.1.

* Tue Jul 14 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-4
- Rebuild for updated dependencies.

* Thu Jul 09 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-3
- Rebuild for updated dependencies.

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-2
- Enable AV1 support also on CentOS/RHEL.

* Tue Jun 23 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-1
- Update to 4.3.
- Enable VMAF support.
- Disable ZeroMQ support on RHEL/CentOS 7."

* Mon Jun 08 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.3-2
- Rebuild for updated dependencies.

* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.3-1
- Update to 4.2.3.
- Update SPEC file.

* Fri May 15 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-6
- Rebuild for updated dependencies.

* Fri Mar 27 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-5
- Enable iec6188 to support DV capure wia Firewire.

* Sun Mar 15 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-4
- Fix build on Fedora 32.

* Sun Jan 19 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-3
- Rebuild for updated dependencies.

* Thu Jan 16 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-2
- Enable vapoursynth on Fedora & RHEL/CentOS 8.

* Sat Jan 11 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-1
- Update to 4.2.2.
