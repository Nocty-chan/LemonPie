from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from ..models import (
    CVEntry,
    GroupEntry,
    GroupEntryLinkedList,
)


class AllGroupsView(generic.ListView):
    template_name = 'resumebuilder/all_groups.html'
    context_object_name = 'group_entry_list'

    def get_queryset(self):
        return GroupEntry.objects.filter()


def list_of_entries_for_group(group_entry):
    head_of_group = group_entry.get_list_head()
    entries_in_group = []
    if head_of_group is not None:
        entries_in_group = [head_of_group]
        while head_of_group.successor is not None:
            entries_in_group = entries_in_group + \
                [head_of_group.successor]
            head_of_group = head_of_group.successor
    return entries_in_group


def group_view(request, group_id):
    group_entry = get_object_or_404(GroupEntry, pk=group_id)
    context = {
        'group_entry': group_entry,
        'cv_entries': list_of_entries_for_group(group_entry),
        'enable_modification': True,
    }
    return render(request, 'resumebuilder/group_entry_base.html', context)


def modify_group(request, group_id):
    group_entry = get_object_or_404(GroupEntry, pk=group_id)
    name = request.POST['group_name']
    if name != "":
        group_entry.name = name
        group_entry.save()
    return HttpResponseRedirect(reverse('resumebuilder:group_view', args=(group_id,)))


def add_new_group(request):
    current_user = get_object_or_404(User, pk=1)
    group_entry = GroupEntry(user=current_user)
    group_entry.save()
    group_entry.name = "Group_Entry_" + str(group_entry.id)
    group_entry.save()
    return group_view(request, group_entry.id)


def delete_group(request, group_id):
    group_entry = get_object_or_404(GroupEntry, pk=group_id)
    group_entry.delete()
    return HttpResponseRedirect(reverse('resumebuilder:all_groups', args=()))


def add_entry_to_group(request, group_id):
    entry_id = request.POST['entry_id']
    cv_entry = get_object_or_404(CVEntry, pk=entry_id)
    group_entry = get_object_or_404(GroupEntry, pk=group_id)
    group_entry.add_entry(cv_entry)
    return HttpResponseRedirect(reverse('resumebuilder:group_view', args=(group_id,)))


def delete_entry_from_group(request, entry_list_id):
    group_entry_pair = get_object_or_404(GroupEntryLinkedList, pk=entry_list_id)
    group_id = group_entry_pair.group_entry.id
    group_entry_pair.delete()
    return HttpResponseRedirect(reverse('resumebuilder:group_view', args=(group_id,)))
