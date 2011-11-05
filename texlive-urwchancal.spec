# revision 21701
# category Package
# catalog-ctan /fonts/urwchancal
# catalog-date 2011-03-10 10:40:13 +0100
# catalog-license lppl
# catalog-version 1
Name:		texlive-urwchancal
Version:	1
Release:	1
Summary:	Use URW's clone of Zapf Chancery as a maths alphabet
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urwchancal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urwchancal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urwchancal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows (the URW clone of) Zapf Chancery to function
as a maths alphabet, the target of \mathcal or \mathscr, with
accents appearing where they should, and other spacing
parameters set to reasonable (not very tight) values.

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
%{_texmfdistdir}/fonts/tfm/urw/urwchancal/urwchancal.tfm
%{_texmfdistdir}/fonts/vf/urw/urwchancal/urwchancal.vf
%{_texmfdistdir}/tex/latex/urwchancal/urwchancal.sty
%{_texmfdistdir}/tex/latex/urwchancal/uurwchancal.fd
%doc %{_texmfdistdir}/doc/fonts/urwchancal/README
%doc %{_texmfdistdir}/doc/fonts/urwchancal/urwchancal-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/urwchancal/urwchancal-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
