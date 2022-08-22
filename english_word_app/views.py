from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import EnglishWordModel


class EnglishWordList(ListView): # リスト一覧
  template_name = 'list.html'
  model = EnglishWordModel


class EnglishWordDetail(DetailView): # リスト詳細
  template_name = 'detail.html'
  model = EnglishWordModel


class EnglishWordCreate(CreateView): # 新規作成
  template_name = 'create.html'
  model = EnglishWordModel
  fields = ('english_word', 'japanese_word')
  success_url = reverse_lazy('list')
  


class EnglishWordDelete(DeleteView): # リスト削除
  template_name = 'delete.html'
  model = EnglishWordModel
  success_url = reverse_lazy('list')


class EnglishWordUpdate(UpdateView): # リスト更新
  template_name = 'update.html'
  model = EnglishWordModel
  fields = ('english_word', 'japanese_word')
  success_url = reverse_lazy('list')


def check_count_func(request, pk):  # カウント数を１増やす
  object = EnglishWordModel.objects.get(pk=pk)
  object.check_count += 1
  object.save()
  return redirect('list')
  