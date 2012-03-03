# -*- coding: utf-8 -*-


def delete_file(sender, instance, **kwargs):
    instance.document.delete(save=False)  # no instance saving aftre deleting file
