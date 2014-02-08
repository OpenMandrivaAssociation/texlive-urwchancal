# revision 21701
# category Package
# catalog-ctan /fonts/urwchancal
# catalog-date 2011-03-10 10:40:13 +0100
# catalog-license lppl
# catalog-version 1
Name:		texlive-urwchancal
Version:	1
Release:	3
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-2
+ Revision: 757330
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 719863
- texlive-urwchancal
- texlive-urwchancal
- texlive-urwchancal

