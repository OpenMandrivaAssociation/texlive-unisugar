# revision 22357
# category Package
# catalog-ctan /macros/xetex/latex/unisugar
# catalog-date 2011-05-08 11:17:43 +0200
# catalog-license lppl1.3
# catalog-version 0.92
Name:		texlive-unisugar
Version:	0.92
Release:	1
Summary:	Define syntactic sugar for Unicode LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/unisugar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unisugar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unisugar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows the user to define shorthand aliases for
single Unicode characters, and also provides support for such
aliases in RTL-text. The package requires an TeX-alike system
that uses Unicode input in a native way: current examples are
XeTeX and LuaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/unisugar/unisugar.sty
%doc %{_texmfdistdir}/doc/xelatex/unisugar/Makefile
%doc %{_texmfdistdir}/doc/xelatex/unisugar/README
%doc %{_texmfdistdir}/doc/xelatex/unisugar/gedit-mixed-sugar.png
%doc %{_texmfdistdir}/doc/xelatex/unisugar/gedit-mixed-traditional.png
%doc %{_texmfdistdir}/doc/xelatex/unisugar/sugar.png
%doc %{_texmfdistdir}/doc/xelatex/unisugar/traditional.png
%doc %{_texmfdistdir}/doc/xelatex/unisugar/unisugar.pdf
%doc %{_texmfdistdir}/doc/xelatex/unisugar/unisugar.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
