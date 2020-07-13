from django.shortcuts import render,HttpResponseRedirect,render_to_response,redirect
from .models import CompteBancaires,Produits,Clients,FacturesProforma,FacturesEdex,FacturesUnpa,List_ProduitsProforma,List_ProduitsEdex,List_ProduitsUnpa
from django.views.generic import ListView
from django.template import RequestContext
from django.contrib import messages
from datetime import datetime
from itertools import chain



class LoginView(ListView):
    template_name='accounts/Login.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class AddBankAccountView(ListView):
    template_name='accounts/AddBankAccount.html'
    def get(self,request,*args, **kwargs):
        addBankAccountPost=CompteBancaires()
        addClientPost=Clients()
        clients_list=Clients.objects.all()
        comptebancaires_list=CompteBancaires.objects.all()
        data={'addBankAccountPost':comptebancaires_list,'addClientsPost':clients_list}
        return render(request,self.template_name,data)
    def post(self,request):
        addBankAccountPost=CompteBancaires()
        addClientPost=Clients()
        clients_list=Clients.objects.all()
        comptebancaires_list=CompteBancaires.objects.all()
        data={'addBankAccountPost':comptebancaires_list,'addClientsPost':clients_list}
        if request.method == 'POST':
            if request.POST.get('B_AN_FR') and request.POST.get('B_AN_EN') and request.POST.get('B_AN_AR') and request.POST.get('B_CS_FR') and request.POST.get('B_CS_EN') and request.POST.get('B_CS_AR') and request.POST.get('B_BA_FR') and request.POST.get('B_BA_EN') and request.POST.get('B_BA_AR'):
                addBankAccountPost.num_b_fr= request.POST.get('B_AN_FR')
                addBankAccountPost.num_b_an= request.POST.get('B_AN_EN')
                addBankAccountPost.num_b_ar= request.POST.get('B_AN_AR')
                addBankAccountPost.code_s_fr= request.POST.get('B_CS_FR')
                addBankAccountPost.code_s_an= request.POST.get('B_CS_EN')
                addBankAccountPost.code_s_ar= request.POST.get('B_CS_AR')
                addBankAccountPost.adresse_b_fr= request.POST.get('B_BA_FR')
                addBankAccountPost.adresse_b_an= request.POST.get('B_BA_EN')
                addBankAccountPost.adresse_b_ar= request.POST.get('B_BA_AR')
                addBankAccountPost.save()
                return HttpResponseRedirect(self.request.path_info)
        else:
            return render(request,self.template_name,data)
        return render(request,self.template_name,data)

class AddClientView(ListView):
    template_name='accounts/AddClient.html'
    def get(self,request,*args, **kwargs):
        addClientPost=Clients()
        clients_list=Clients.objects.all()
        data={'addClientPost':clients_list,}
        return render(request,self.template_name,data)
    def post(self,request):
        addClientPost=Clients()
        clients_list=Clients.objects.all()
        data={'addClientPost':clients_list,}
        if request.method == 'POST':
            if request.POST.get('C_N_FR') and request.POST.get('C_A_FR') and request.POST.get('C_N_EN') and request.POST.get('C_A_EN') and request.POST.get('C_N_AR') and request.POST.get('C_A_AR') :
                addClientPost.nom_fr= request.POST.get('C_N_FR')
                addClientPost.adresse_fr= request.POST.get('C_A_FR')
                addClientPost.nom_an= request.POST.get('C_N_EN')
                addClientPost.adresse_an= request.POST.get('C_A_EN')
                addClientPost.nom_ar= request.POST.get('C_N_AR')
                addClientPost.adresse_ar= request.POST.get('C_A_AR')
                addClientPost.numero= request.POST.get('C_PN_EN')
                addClientPost.email= request.POST.get('C_E_EN')
                addClientPost.save()
                return HttpResponseRedirect(self.request.path_info)
        else:
            return render(request,self.template_name,data)
        return render(request,self.template_name,data)

class AddProductView(ListView):
    template_name='accounts/AddProduct.html'
    def get(self,request,*args, **kwargs):
        addProductPost=Produits()
        produits_list=Produits.objects.all()
        data={'addProductPost':produits_list}
        return render(request,self.template_name,data)
    def post(self,request):
        addProductPost=Produits()
        produits_list=Produits.objects.all()
        data={'addProductPost':produits_list}
        if request.method == 'POST':
            if request.POST.get('P_D_FR') and request.POST.get('P_D_EN') and request.POST.get('P_D_AR') and request.POST.get('P_PU_FR') and request.POST.get('P_PU_EN') and request.POST.get('P_PU_AR'):
                addProductPost.designation_fr= request.POST.get('P_D_FR')
                addProductPost.designation_an= request.POST.get('P_D_EN')
                addProductPost.designation_ar= request.POST.get('P_D_AR')
                addProductPost.prix_u_fr= request.POST.get('P_PU_FR')
                addProductPost.prix_u_an= request.POST.get('P_PU_EN')
                addProductPost.prix_u_ar= request.POST.get('P_PU_AR')
                addProductPost.save()
                return HttpResponseRedirect(self.request.path_info)
        else:
            return render(request,self.template_name,data)
        return render(request,self.template_name,data)

class HomeView(ListView):
    template_name='accounts/Home.html'
    def get(self,request,*args, **kwargs):
        FacturesEdexPost=FacturesEdex()
        facturesEdex_list=FacturesEdex.objects.all()
        FacturesUnpaPost=FacturesUnpa()
        facturesUnpa_list=FacturesUnpa.objects.all()
        FacturesProformaPost=FacturesProforma()
        facturesProforma_list=FacturesProforma.objects.all()
        data={'FacturesEdexPost':facturesEdex_list,'FacturesUnpaPost':facturesUnpa_list,'FacturesProformaPost':facturesProforma_list,}
        return render(request,self.template_name,data)

    def post(self,request):
        buttonAn=request.POST.get("buttonAn")
        buttonFr=request.POST.get("buttonFr")
        buttonAr=request.POST.get("buttonAr")
        ChoixProforma=request.POST.get("ChoixProforma")
        ChoixUNPA=request.POST.get("ChoixUNPA")
        ChoixEdex=request.POST.get("ChoixEdex")
        buttonSuppPro=request.POST.get("buttonSuppPro")
        buttonSuppEdex=request.POST.get("buttonSuppEdex")
        buttonSuppUnpa=request.POST.get("buttonSuppUnpa")
        ProduitsPost=Produits()
        ClientsPost=Clients()
        ComptebancairesPost=CompteBancaires()
        if(buttonSuppPro):
            FacturesProforma.objects.filter(id_f=ChoixProforma).delete()
            return HttpResponseRedirect(self.request.path_info)
        elif(buttonSuppUnpa):
            FacturesUnpa.objects.filter(id_f=ChoixUNPA).delete()
            return HttpResponseRedirect(self.request.path_info)
        elif(buttonSuppEdex):
            FacturesEdex.objects.filter(id_f=ChoixEdex).delete()
            return HttpResponseRedirect(self.request.path_info)
        if(ChoixEdex):
            print("Edex")
            FacturesPost=FacturesEdex()
            ListProduitsPost=List_ProduitsEdex()
            clients_list=Clients.objects.filter(id_c_l=FacturesEdex.objects.filter(id_f=request.POST.get("ChoixEdex"))[0].id_c_f.id_c_l)
            Comptebancaires_list=CompteBancaires.objects.filter(id_c_b=FacturesEdex.objects.filter(id_f=request.POST.get("ChoixEdex"))[0].id_c_b_f.id_c_b)
            factures_list=FacturesEdex.objects.filter(id_f=request.POST.get("ChoixEdex"))
            list_produits_list=List_ProduitsEdex.objects.filter(id_fa=request.POST.get("ChoixEdex"))
            print("affich")
            produits_list=[]
            pp=Produits.objects.none()
            i=0
            for e in List_ProduitsEdex.objects.filter(id_fa=request.POST.get("ChoixEdex")):
                produits_list.append(Produits.objects.filter(id_c_p=e.id_p.id_c_p))
                print(i," ",produits_list[i])
                i += 1
            for x in produits_list:
                print(x)
                pp=list(chain(pp,x))
            for e in pp:
                print(e.designation_an)
            data={'FacturesPost':factures_list,'ListProduitsPost':list_produits_list,'ProduitsPost':pp,'ClientsPost':clients_list,'CompteBancairesPost':Comptebancaires_list}
            if buttonAn:
                return render(request,'accounts/FactureEdexAn.html',data)
            if buttonFr:
                return render(request,'accounts/FactureEdexFr.html',data)
            if buttonAr:
                return render(request,'accounts/FactureEdexAr.html',data)
        if(ChoixUNPA):
            print("Unpa")
            FacturesPost=FacturesUnpa()
            ListProduitsUnpaPost=List_ProduitsUnpa()
            clients_list=Clients.objects.filter(id_c_l=FacturesUnpa.objects.filter(id_f=request.POST.get("ChoixUNPA"))[0].id_c_f.id_c_l)
            Comptebancaires_list=CompteBancaires.objects.filter(id_c_b=FacturesUnpa.objects.filter(id_f=request.POST.get("ChoixUNPA"))[0].id_c_b_f.id_c_b)
            factures_list=FacturesUnpa.objects.filter(id_f=request.POST.get("ChoixUNPA"))
            list_produits_list=List_ProduitsUnpa.objects.filter(id_fa=request.POST.get("ChoixUNPA"))
            print("affich")
            produits_list=[]
            pp=Produits.objects.none()
            i=0
            for e in List_ProduitsUnpa.objects.filter(id_fa=request.POST.get("ChoixUNPA")):
                produits_list.append(Produits.objects.filter(id_c_p=e.id_p.id_c_p))
                print(i," ",produits_list[i])
                i += 1
            for x in produits_list:
                print(x)
                pp=list(chain(pp,x))
            for e in pp:
                print(e.designation_an)
            data={'FacturesPost':factures_list,'ListProduitsPost':list_produits_list,'ProduitsPost':pp,'ClientsPost':clients_list,'CompteBancairesPost':Comptebancaires_list}
            if buttonAn:
                return render(request,'accounts/FactureUnpaAn.html',data)
            if buttonFr:
                return render(request,'accounts/FactureUnpaFr.html',data)
            if buttonAr:
                return render(request,'accounts/FactureUnpaAr.html',data)
        if(ChoixProforma):
            print("Proforma")
            FacturesPost=FacturesProforma()
            ListProduitsPost=List_ProduitsProforma()
            clients_list=Clients.objects.filter(id_c_l=FacturesProforma.objects.filter(id_f=request.POST.get("ChoixProforma"))[0].id_c_f.id_c_l)
            Comptebancaires_list=CompteBancaires.objects.filter(id_c_b=FacturesProforma.objects.filter(id_f=request.POST.get("ChoixProforma"))[0].id_c_b_f.id_c_b)
            factures_list=FacturesProforma.objects.filter(id_f=request.POST.get("ChoixProforma"))
            list_produits_list=List_ProduitsProforma.objects.filter(id_fa=request.POST.get("ChoixProforma"))
            print("affich")
            produits_list=[]
            pp=Produits.objects.none()
            i=0
            for e in List_ProduitsProforma.objects.filter(id_fa=request.POST.get("ChoixProforma")):
                produits_list.append(Produits.objects.filter(id_c_p=e.id_p.id_c_p))
                print(i," ",produits_list[i])
                i += 1
            for x in produits_list:
                print(x)
                pp=list(chain(pp,x))
            for e in pp:
                print(e.designation_an)
            data={'FacturesPost':factures_list,'ListProduitsPost':list_produits_list,'ProduitsPost':pp,'ClientsPost':clients_list,'CompteBancairesPost':Comptebancaires_list}
            if buttonAn:
                return render(request,'accounts/FactureProformaAn.html',data)
            if buttonFr:
                return render(request,'accounts/FactureProformaFr.html',data)
            if buttonAr:
                return render(request,'accounts/FactureProformaAr.html',data)

class InvoiceRegisterView(ListView):
    template_name='accounts/InvoiceRegister.html'

    def get(self,request,*args, **kwargs):
        addBankAccountPost=CompteBancaires()
        addClientPost=Clients()
        addProductPost=Produits()
        addProductListPost=List_ProduitsProforma()
        comptebancaires_list=CompteBancaires.objects.all()
        clients_list=Clients.objects.all()
        produits_list=Produits.objects.all()
        data={'addBankAccountPost':comptebancaires_list,'addClientPost':clients_list,'addProductPost':produits_list}
        return render(request,self.template_name,data)
    def post(self,request):
        addBankAccountPost=CompteBancaires()
        addClientPost=Clients()
        addProductPost=Produits()
        comptebancaires_list=CompteBancaires.objects.all()
        clients_list=Clients.objects.all()
        produits_list=Produits.objects.all()
        ChoixType=request.POST.get('ChoixType')
        if(ChoixType=="Pro forma"):
            invoiceRegisterPost=FacturesProforma()
            invoiceRegisterPost.type=ChoixType
            invoiceRegister_list=FacturesProforma.objects.all()
            addProductListPost=List_ProduitsProforma()
        elif(ChoixType=="UNPA"):
            invoiceRegisterPost=FacturesUnpa()
            invoiceRegisterPost.type=ChoixType
            invoiceRegister_list=FacturesProforma.objects.all()
            addProductListPost=List_ProduitsUnpa()
        elif(ChoixType=="EDEX"):
            invoiceRegisterPost=FacturesEdex()
            invoiceRegisterPost.type=ChoixType
            invoiceRegister_list=FacturesProforma.objects.all()
            addProductListPost=List_ProduitsEdex()
        if request.method == 'POST':
            try:
                invoiceRegisterPost.poids_net=float(request.POST.get('IR_PN'))
            except ValueError:
                invoiceRegisterPost.poids_net=0
            try:
                invoiceRegisterPost.poids_brut=float(request.POST.get('IR_PB'))
            except ValueError:
                invoiceRegisterPost.poids_brut=0
            try:
                invoiceRegisterPost.id_c_b_f=CompteBancaires.objects.get(id_c_b=request.POST.get('IR_BA'))
            except CompteBancaires.DoesNotExist:
                invoiceRegisterPost.id_c_b_f=None
            try:
                invoiceRegisterPost.id_c_f=Clients.objects.get(id_c_l=request.POST.get('IR_IDC'))
            except Clients.DoesNotExist:
                invoiceRegisterPost.id_c_f=None
            invoiceRegisterPost.destination=request.POST.get('IR_D')
            invoiceRegisterPost.mode_livraison=request.POST.get('IR_ML')
            invoiceRegisterPost.port_chargement=request.POST.get('IR_PC')
            invoiceRegisterPost.pays_origine=request.POST.get('IR_PO')
            invoiceRegisterPost.nb_conteneur=request.POST.get('IR_NCn')
            invoiceRegisterPost.ngp=request.POST.get('IR_NGP')
            invoiceRegisterPost.mode_paiement=request.POST.get('IR_MP')
            invoiceRegisterPost.o_t_fr=request.POST.get('OT_Fr')
            invoiceRegisterPost.o_c_fr=request.POST.get('OC_Fr')
            invoiceRegisterPost.o_t_an=request.POST.get('OT_An')
            invoiceRegisterPost.o_c_an=request.POST.get('OC_An')
            invoiceRegisterPost.o_t_ar=request.POST.get('OT_Ar')
            invoiceRegisterPost.o_c_ar=request.POST.get('OC_Ar')
            invoiceRegisterPost.os_t_fr=request.POST.get('OT_Fr_S')
            invoiceRegisterPost.os_c_fr=request.POST.get('OC_Fr_S')
            invoiceRegisterPost.os_t_an=request.POST.get('OT_An_S')
            invoiceRegisterPost.os_c_an=request.POST.get('OC_An_S')
            invoiceRegisterPost.os_t_ar=request.POST.get('OT_Ar_S')
            invoiceRegisterPost.os_c_ar=request.POST.get('OC_Ar_S')
            invoiceRegisterPost.ot_t_fr=request.POST.get('OT_Fr_T')
            invoiceRegisterPost.ot_c_fr=request.POST.get('OC_Fr_T')
            invoiceRegisterPost.ot_t_an=request.POST.get('OT_An_T')
            invoiceRegisterPost.ot_c_an=request.POST.get('OC_An_T')
            invoiceRegisterPost.ot_t_ar=request.POST.get('OT_Ar_T')
            invoiceRegisterPost.ot_c_ar=request.POST.get('OC_Ar_T')
            invoiceRegisterPost.prix_t_lettres_fr=request.POST.get('IR_TPL_Fr')
            invoiceRegisterPost.prix_t_lettres_an=request.POST.get('IR_TPL_An')
            invoiceRegisterPost.prix_t_lettres_ar=request.POST.get('IR_TPL_Ar')
            invoiceRegisterPost.code_date=invoiceRegisterPost.date.strftime('%y')
            try:
                invoiceRegisterPost.code=int(request.POST.get('IR_C'))
            except ValueError:
                invoiceRegisterPost.code=0
            invoiceRegisterPost.save()
            if int(request.POST.get('tot'))==0:
                print("Il n'ya aucun produits")
            else:
                total=0
                total_collis=0
                for x in range(0,int(request.POST.get('inc'))+1):
                    if(request.POST.get("LP_P"+str(x))==None):
                        pass
                    else:
                        if(ChoixType=="Pro forma"):
                            addProductListPost=List_ProduitsProforma()
                            addProductListPost.id_fa=FacturesProforma.objects.get(id_f=FacturesProforma.objects.latest('id_f').id_f)
                        elif(ChoixType=="UNPA"):
                            addProductListPost=List_ProduitsUnpa()
                            addProductListPost.id_fa=FacturesUnpa.objects.get(id_f=FacturesUnpa.objects.latest('id_f').id_f)
                        elif(ChoixType=="EDEX"):
                            addProductListPost=List_ProduitsEdex()
                            addProductListPost.id_fa=FacturesEdex.objects.get(id_f=FacturesEdex.objects.latest('id_f').id_f)
                        addProductListPost.id_p=Produits.objects.get(id_c_p=request.POST.get('LP_IP'+str(x)))
                        try:
                            addProductListPost.poids=float(request.POST.get("LP_P"+str(x)))
                        except (ValueError,TypeError):
                            addProductListPost.poids=0
                        try:
                            addProductListPost.collis=int(request.POST.get("LP_C"+str(x)))
                        except (ValueError,TypeError):
                            addProductListPost.collis=0
                        addProductListPost.prix_t=float(addProductListPost.id_p.prix_u_fr)*float(addProductListPost.poids)
                        total=total+addProductListPost.prix_t
                        total_collis=total_collis+addProductListPost.collis
                        addProductListPost.save()
            try:
                invoiceRegisterPost.prix_t=total
            except ValueError:
                invoiceRegisterPost.prix_t=0
            try:
                invoiceRegisterPost.nb_colis=total_collis
            except ValueError:
                invoiceRegisterPost.nb_colis=0
            invoiceRegisterPost.save()
            data={'addBankAccountPost':comptebancaires_list,'addClientPost':clients_list,'addProductPost':produits_list}
            return render(request,self.template_name,data)
        else:
            return render(request,self.template_name,data)
            data={'addBankAccountPost':comptebancaires_list,'addClientPost':clients_list,'addProductPost':produits_list}
        data={'addBankAccountPost':comptebancaires_list,'addClientPost':clients_list,'addProductPost':produits_list}
        return render(request,self.template_name,data)

class FactureEdexAnView(ListView):
    template_name='accounts/FactureEdexAn.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureEdexFrView(ListView):
    template_name='accounts/FactureEdexFr.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureEdexArView(ListView):
    template_name='accounts/FactureEdexAr.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureProformaAnView(ListView):
    template_name='accounts/FactureProformaAn.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureProformaFrView(ListView):
    template_name='accounts/FactureProformaFr.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureProformaArView(ListView):
    template_name='accounts/FactureProformaAr.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureUnpaAnView(ListView):
    template_name='accounts/FactureUnpaAn.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureUnpaFrView(ListView):
    template_name='accounts/FactureUnpaFr.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class FactureUnpaArView(ListView):
    template_name='accounts/FactureUnpaAr.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)
