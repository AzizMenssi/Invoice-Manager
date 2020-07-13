from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from main.views import LoginView,AddClientView,AddProductView,AddBankAccountView,HomeView,InvoiceRegisterView,FactureEdexAnView,FactureEdexFrView,FactureEdexArView,FactureProformaAnView,FactureProformaFrView,FactureProformaArView,FactureUnpaAnView,FactureUnpaFrView,FactureUnpaArView
urlpatterns = [
    url(r'^$',login,{'template_name':'accounts/Login.html'}),
    url(r'^Login/$',LoginView.as_view(),name='LoginView'),
    url(r'^Home/$',HomeView.as_view(),name='HomeView'),
    url(r'^Home/AddBankAccount/$',AddBankAccountView.as_view(),name='AddBankAccountView'),
    url(r'^Home/AddClient/$',AddClientView.as_view(),name='AddClientView'),
    url(r'^Home/AddProduct/$',AddProductView.as_view(),name='AddProductView'),
    url(r'^Home/InvoiceRegister/$',InvoiceRegisterView.as_view(),name='InvoiceRegisterView'),
    url(r'^Home/FactureAr/$',FactureEdexAnView.as_view(),name='FactureEdexAnView'),
    url(r'^Home/FactureFr/$',FactureEdexFrView.as_view(),name='FactureEdexFrView'),
    url(r'^Home/FactureAn/$',FactureEdexArView.as_view(),name='FactureEdexArView'),
    url(r'^Home/FactureAr/$',FactureProformaAnView.as_view(),name='FactureProformaAnView'),
    url(r'^Home/FactureFr/$',FactureProformaFrView.as_view(),name='FactureProformaFrView'),
    url(r'^Home/FactureAn/$',FactureProformaArView.as_view(),name='FactureProformaArView'),
    url(r'^Home/FactureAr/$',FactureUnpaAnView.as_view(),name='FactureUnpaAnView'),
    url(r'^Home/FactureFr/$',FactureUnpaFrView.as_view(),name='FactureUnpaFrView'),
    url(r'^Home/FactureAn/$',FactureUnpaArView.as_view(),name='FactureUnpaArView'),
]
