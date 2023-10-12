from django.db import models
from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from .models import Entry, PassDown
from UserBase.models import WorkCenter
from .forms import PassDownForm, EntryForm
from django.urls import reverse
from django.views.generic import (
    CreateView, ListView, DetailView, TemplateView, UpdateView,
    DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class EntryCreateView(LoginRequiredMixin, CreateView):
    template_name = "passdown/entry_create.html"
    form_class = EntryForm
    context_object_name = 'passdown'

    def get_queryset(self):
        queryset = PassDown.objects.last()
        return queryset

    def get_success_url(self):
        return reverse("passdown:entry-create")


class PassDownCreateView(LoginRequiredMixin, CreateView):
    template_name = "passdown/passdown_create.html"
    form_class = PassDownForm

    def form_valid(self, form):
        entered = form.save(commit=False)
        entered.entered_by = self.request.user
        entered.save()
        return super(PassDownCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse("passdown:entry-create")


class EntryByPassdown(LoginRequiredMixin, ListView):
    template_name = "passdown/entry_by_passdown.html"
    context_object_name = "entries"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['queryset1'] = Entry.objects.filter(passdown_id=kwargs)
        return context_data

    def get_queryset(self):
        myset = {
            "queryset1": Entry.objects.filter(passdown_id=1),
            "queryset2": PassDown.objects.filter(id=1)
        }
        return myset
    

class PassDownListView(LoginRequiredMixin, ListView):
    template_name = "passdown/passdown_list.html"
    context_object_name = "entries"

    # def get_context_data(self, **kwargs):
    #     context_data = super(QueryTest, self).get_context_data(**kwargs)
    #     return context_data

    def get_queryset(self):
        queryset = PassDown.objects.all().order_by("date_time")
        return queryset
    

class PassDownDetailView(LoginRequiredMixin, ListView):
    template_name = "passdown/passdown_detail_test.html"
    context_object_name = "entries"

    def get_queryset(self):
        queryset = PassDown.objects.all()
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(PassDownDetailView, self).get_context_data(**kwargs)
        pd = PassDown.objects.get(pk=self.kwargs['pk'])
        queryset2 = pd.entry_set.all()
        context.update({
            "individual_entries": queryset2,
            "parent_passdown": pd,
        })
        return context


class EntryListView(LoginRequiredMixin, ListView):
    template_name = "passdown/entry_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        QuerySet = Entry.objects.all()
        return QuerySet


class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'passdown/dashboard.html'
    context_object_name = 'entries'

    def get_queryset(self):
        queryset = PassDown.objects.last()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        pd = PassDown.objects.latest('id')
        queryset2 = pd.entry_set.all().order_by('modex')
        context.update({
            "individual_entries": queryset2,
            "parent_passdown": pd,
        })
        return context
    
class MasterListView(LoginRequiredMixin, ListView):
    template_name = 'passdown/master_list.html'
    context_object_name = 'entries'

    def nested_query_loop(self):
        object_list = []
        all_objects = PassDown.objects.all() #queryset containing all passdown objects
        for object in all_objects:
            object_list.append(object.pk) #list containing all passdown primary keys (object_list)

        query_dict={}
        for i in object_list:
            temp_obj = PassDown.objects.get(pk=i) #ith passdown object itself
            sub_object_pk_list=[]
            all_i_entries = temp_obj.entry_set.all() #queryset containing all entry objects of i
            for j in all_i_entries:
                sub_object_pk_list.append(j.pk) #list containing all entry primary keys of i (sub_object_pk_list)
                
            sub_object_list = []
            for k in sub_object_pk_list:
                sub_object_list.append(all_i_entries.get(pk=k)) #list containing all ith entry objects (sub_object_list)
            query_dict.__setitem__(temp_obj, sub_object_list)

        return query_dict

    def get_queryset(self):
        queryset = PassDown.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(MasterListView, self).get_context_data(**kwargs)
        queryset = self.nested_query_loop()
        context.update({
            "parent_child_dict": queryset
        })
        return context
    
class MasterListView2(LoginRequiredMixin, ListView):
    template_name = 'passdown/master_list2.html'
    model = PassDown
    paginate_by = 5
    context_object_name = 'entries'


    def get_queryset(self):
        queryset = PassDown.objects.all().order_by("-date_time")
        return queryset
    
class SearchResultsView(LoginRequiredMixin, ListView):
    template_name = 'passdown/search_results.html'
    model = PassDown
    paginate_by = 5
    context_object_name = 'entries'
    form_class = EntryForm

    def get_queryset(self):
        modex = self.request.GET.get('modex')
        shift = self.request.GET.get('shift')
        keyword = self.request.GET.get('keyword')
        job_status = self.request.GET.get('jobstatus')
        #cdi = self.request.GET.get('cdi')
        discrepancy = self.request.GET.get('discrepancy')
        queryset = PassDown.objects.filter(
            Q(entry__modex__icontains=modex),
            Q(shift__icontains=shift),
            Q(entry__text_body__icontains=keyword),
            #Q(entry__job_status__icontains=job_status),
            #Q(entry__cdi__icontains=cdi),
            Q(entry__discrepancy__icontains=discrepancy)
            )
        return queryset

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'passdown/search.html'

class SearchTestView(LoginRequiredMixin, FormView):
    template_name = 'passdown/search_test.html'
    form_class = EntryForm

class AdminDashboardView(LoginRequiredMixin, ListView):
     template_name = 'passdown/admin_dashboard.html'
     model = WorkCenter
     context_object_name = 'workcenter'
