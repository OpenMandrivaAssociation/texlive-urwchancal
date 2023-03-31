Name:		texlive-urwchancal
Version:	21701
Release:	2
Summary:	Use URW's clone of Zapf Chancery as a maths alphabet
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urwchancal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urwchancal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urwchancal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows (the URW clone of) Zapf Chancery to function
as a maths alphabet, the target of \mathcal or \mathscr, with
accents appearing where they should, and other spacing
parameters set to reasonable (not very tight) values.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
