exec("import re;import base64");exec(base64.b64decode("IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KCiIiIgpDb3B5cmlnaHQgKEMpIDIwMTUKClRoaXMgcHJvZ3JhbSBpcyBmcmVlIHNvZnR3YXJlOiB5b3UgY2FuIHJlZGlzdHJpYnV0ZSBpdCBhbmQvb3IgbW9kaWZ5Cml0IHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgYXMgcHVibGlzaGVkIGJ5CnRoZSBGcmVlIFNvZnR3YXJlIEZvdW5kYXRpb24sIGVpdGhlciB2ZXJzaW9uIDMgb2YgdGhlIExpY2Vuc2UsIG9yCihhdCB5b3VyIG9wdGlvbikgYW55IGxhdGVyIHZlcnNpb24uCgpUaGlzIHByb2dyYW0gaXMgZGlzdHJpYnV0ZWQgaW4gdGhlIGhvcGUgdGhhdCBpdCB3aWxsIGJlIHVzZWZ1bCwKYnV0IFdJVEhPVVQgQU5ZIFdBUlJBTlRZOyB3aXRob3V0IGV2ZW4gdGhlIGltcGxpZWQgd2FycmFudHkgb2YKTUVSQ0hBTlRBQklMSVRZIG9yIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFLiAgU2VlIHRoZQpHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBmb3IgbW9yZSBkZXRhaWxzLgoKWW91IHNob3VsZCBoYXZlIHJlY2VpdmVkIGEgY29weSBvZiB0aGUgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UKYWxvbmcgd2l0aCB0aGlzIHByb2dyYW0uIElmIG5vdCwgc2VlIDxodHRwOi8vd3d3LmdudS5vcmcvbGljZW5zZXMvPgoiIiIKCmltcG9ydCB1cmxsaWIsIHVybGxpYjIsIHN5cywgcmUsIG9zLCB1bmljb2RlZGF0YQppbXBvcnQgeGJtYywgeGJtY2d1aSwgeGJtY3BsdWdpbiwgeGJtY2FkZG9uCmltcG9ydCBiYXNlNjQKCnBsdWdpbl9oYW5kbGUgPSBpbnQoc3lzLmFyZ3ZbMV0pCgpteXNldHRpbmdzID0geGJtY2FkZG9uLkFkZG9uKGlkID0gJ3BsdWdpbi52aWRlby5wZXRyaW5qYScpCnByb2ZpbGUgPSBteXNldHRpbmdzLmdldEFkZG9uSW5mbygncHJvZmlsZScpCmhvbWUgPSBteXNldHRpbmdzLmdldEFkZG9uSW5mbygncGF0aCcpCmZhbmFydCA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oaG9tZSwgJ2ZhbmFydC5qcGcnKSkKaWNvbiA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oaG9tZSwgJ2ljb24ucG5nJykpCgpvbmxpbmVfbTN1ID0gYmFzZTY0LmI2NGRlY29kZSgiYUhSMGNITTZMeTlsYm1NdGFYUXVhSEl2Y0dWMGNtbHVhbUV1YlROMSIpCmxvY2FsX20zdSA9IG15c2V0dGluZ3MuZ2V0U2V0dGluZygnbG9jYWxfbTN1JykKb25saW5lX3htbCA9IG15c2V0dGluZ3MuZ2V0U2V0dGluZygnb25saW5lX3htbCcpCmxvY2FsX3htbCA9IG15c2V0dGluZ3MuZ2V0U2V0dGluZygnbG9jYWxfeG1sJykKCnhtbF9yZWdleCA9ICc8dGl0bGU+KC4qPyk8L3RpdGxlPlxzKjxsaW5rPiguKj8pPC9saW5rPlxzKjx0aHVtYm5haWw+KC4qPyk8L3RodW1ibmFpbD4nCm0zdV90aHVtYl9yZWdleCA9ICd0dmctbG9nbz1bXCciXSguKj8pW1wnIl0nCm0zdV9yZWdleCA9ICcjKC4rPyksKC4rKVxzKiguKylccyonCgp1X3R1YmUgPSAnaHR0cDovL3d3dy55b3V0dWJlLmNvbScKCmRlZiByZW1vdmVBY2NlbnRzKHMpOgoJcmV0dXJuICcnLmpvaW4oKGMgZm9yIGMgaW4gdW5pY29kZWRhdGEubm9ybWFsaXplKCdORkQnLCBzLmRlY29kZSgndXRmLTgnKSkgaWYgdW5pY29kZWRhdGEuY2F0ZWdvcnkoYykgIT0gJ01uJykpCgkJCQkJCmRlZiByZWFkX2ZpbGUoZmlsZSk6CiAgICB0cnk6CiAgICAgICAgZiA9IG9wZW4oZmlsZSwgJ3InKQogICAgICAgIGNvbnRlbnQgPSBmLnJlYWQoKQogICAgICAgIGYuY2xvc2UoKQogICAgICAgIHJldHVybiBjb250ZW50CiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKZGVmIG1ha2VfcmVxdWVzdCh1cmwpOgoJdHJ5OgoJCXJlcSA9IHVybGxpYjIuUmVxdWVzdCh1cmwpCgkJcmVxLmFkZF9oZWFkZXIoJ1VzZXItQWdlbnQnLCAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NDsgcnY6MTkuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xOS4wJykKCQlyZXNwb25zZSA9IHVybGxpYjIudXJsb3BlbihyZXEpCSAgCgkJbGluayA9IHJlc3BvbnNlLnJlYWQoKQoJCXJlc3BvbnNlLmNsb3NlKCkgIAoJCXJldHVybiBsaW5rCglleGNlcHQgdXJsbGliMi5VUkxFcnJvciwgZToKCQlwcmludCAnV2UgZmFpbGVkIHRvIG9wZW4gIiVzIi4nICUgdXJsCgkJaWYgaGFzYXR0cihlLCAnY29kZScpOgoJCQlwcmludCAnV2UgZmFpbGVkIHdpdGggZXJyb3IgY29kZSAtICVzLicgJSBlLmNvZGUJCgkJaWYgaGFzYXR0cihlLCAncmVhc29uJyk6CgkJCXByaW50ICdXZSBmYWlsZWQgdG8gcmVhY2ggYSBzZXJ2ZXIuJwoJCQlwcmludCAnUmVhc29uOiAnLCBlLnJlYXNvbgoJCQkKZGVmIG1haW4oKToKCWlmIGxlbihvbmxpbmVfbTN1KSA+IDA6CQoJCWFkZF9kaXIoJ1tDT0xPUiB5ZWxsb3ddW0JdPj4gSVBUViBQRVRSSU5KQSAtIExJVkUgTElTVEEgPDxbL0JdWy9DT0xPUl0nLCB1X3R1YmUsIDIsIGljb24sIGZhbmFydCkKZGVmIHNlYXJjaCgpOiAJCgl0cnk6CgkJa2V5YiA9IHhibWMuS2V5Ym9hcmQoJycsICdFbnRlciBzZWFyY2ggdGV4dCcpCgkJa2V5Yi5kb01vZGFsKCkKCQlpZiAoa2V5Yi5pc0NvbmZpcm1lZCgpKToKCQkJc2VhcmNoVGV4dCA9IHVybGxpYi5xdW90ZV9wbHVzKGtleWIuZ2V0VGV4dCgpKS5yZXBsYWNlKCcrJywgJyAnKQoJCWlmIGxlbihvbmxpbmVfbTN1KSA+IDA6CQkKCQkJY29udGVudCA9IG1ha2VfcmVxdWVzdChvbmxpbmVfbTN1KQoJCQltYXRjaCA9IHJlLmNvbXBpbGUobTN1X3JlZ2V4KS5maW5kYWxsKGNvbnRlbnQpCgkJCWZvciB0aHVtYiwgbmFtZSwgdXJsIGluIG1hdGNoOgoJCQkJaWYgcmUuc2VhcmNoKHNlYXJjaFRleHQsIHJlbW92ZUFjY2VudHMobmFtZS5yZXBsYWNlKCfEkCcsICdEJykpLCByZS5JR05PUkVDQVNFKToKCQkJCQltM3VfcGxheWxpc3QobmFtZSwgdXJsLCB0aHVtYikJCgkJaWYgbGVuKGxvY2FsX20zdSkgPiAwOgkJCgkJCWNvbnRlbnQgPSByZWFkX2ZpbGUobG9jYWxfbTN1KQoJCQltYXRjaCA9IHJlLmNvbXBpbGUobTN1X3JlZ2V4KS5maW5kYWxsKGNvbnRlbnQpCQkKCQkJZm9yIHRodW1iLCBuYW1lLCB1cmwgaW4gbWF0Y2g6CgkJCQlpZiByZS5zZWFyY2goc2VhcmNoVGV4dCwgcmVtb3ZlQWNjZW50cyhuYW1lLnJlcGxhY2UoJ8SQJywgJ0QnKSksIHJlLklHTk9SRUNBU0UpOgoJCQkJCW0zdV9wbGF5bGlzdChuYW1lLCB1cmwsIHRodW1iKQkKCQlpZiBsZW4ob25saW5lX3htbCkgPiAwOgkJCQkJCgkJCWNvbnRlbnQgPSBtYWtlX3JlcXVlc3Qob25saW5lX3htbCkKCQkJbWF0Y2ggPSByZS5jb21waWxlKHhtbF9yZWdleCkuZmluZGFsbChjb250ZW50KQkKCQkJZm9yIG5hbWUsIHVybCwgdGh1bWIgaW4gbWF0Y2g6CgkJCQlpZiByZS5zZWFyY2goc2VhcmNoVGV4dCwgcmVtb3ZlQWNjZW50cyhuYW1lLnJlcGxhY2UoJ8SQJywgJ0QnKSksIHJlLklHTk9SRUNBU0UpOgoJCQkJCXhtbF9wbGF5bGlzdChuYW1lLCB1cmwsIHRodW1iKQkKCQlpZiBsZW4obG9jYWxfeG1sKSA+IDA6CQkKCQkJY29udGVudCA9IHJlYWRfZmlsZShsb2NhbF94bWwpCgkJCW1hdGNoID0gcmUuY29tcGlsZSh4bWxfcmVnZXgpLmZpbmRhbGwoY29udGVudCkJCQoJCQlmb3IgbmFtZSwgdXJsLCB0aHVtYiBpbiBtYXRjaDoKCQkJCWlmIHJlLnNlYXJjaChzZWFyY2hUZXh0LCByZW1vdmVBY2NlbnRzKG5hbWUucmVwbGFjZSgnxJAnLCAnRCcpKSwgcmUuSUdOT1JFQ0FTRSk6CgkJCQkJeG1sX3BsYXlsaXN0KG5hbWUsIHVybCwgdGh1bWIpCQoJZXhjZXB0OgoJCXBhc3MKCQkKZGVmIG0zdV9vbmxpbmUoKToJCQoJY29udGVudCA9IG1ha2VfcmVxdWVzdChvbmxpbmVfbTN1KQoJbWF0Y2ggPSByZS5jb21waWxlKG0zdV9yZWdleCkuZmluZGFsbChjb250ZW50KQoJZm9yIHRodW1iLCBuYW1lLCB1cmwgaW4gbWF0Y2g6CgkJdHJ5OgoJCQltM3VfcGxheWxpc3QobmFtZSwgdXJsLCB0aHVtYikKCQlleGNlcHQ6CgkJCXBhc3MKCQkJCmRlZiB4bWxfb25saW5lKCk6CQkJCgljb250ZW50ID0gbWFrZV9yZXF1ZXN0KG9ubGluZV94bWwpCgltYXRjaCA9IHJlLmNvbXBpbGUoeG1sX3JlZ2V4KS5maW5kYWxsKGNvbnRlbnQpCglmb3IgbmFtZSwgdXJsLCB0aHVtYiBpbiBtYXRjaDoKCQl0cnk6CgkJCXhtbF9wbGF5bGlzdChuYW1lLCB1cmwsIHRodW1iKQoJCWV4Y2VwdDoKCQkJcGFzcwoJCQkKZGVmIG0zdV9sb2NhbCgpOgoJY29udGVudCA9IHJlYWRfZmlsZShsb2NhbF9tM3UpCgltYXRjaCA9IHJlLmNvbXBpbGUobTN1X3JlZ2V4KS5maW5kYWxsKGNvbnRlbnQpCglmb3IgdGh1bWIsIG5hbWUsIHVybCBpbiBtYXRjaDoJCgkJdHJ5OgoJCQltM3VfcGxheWxpc3QobmFtZSwgdXJsLCB0aHVtYikKCQlleGNlcHQ6CgkJCXBhc3MKCmRlZiB4bWxfbG9jYWwoKToJCQoJY29udGVudCA9IHJlYWRfZmlsZShsb2NhbF94bWwpCgltYXRjaCA9IHJlLmNvbXBpbGUoeG1sX3JlZ2V4KS5maW5kYWxsKGNvbnRlbnQpCglmb3IgbmFtZSwgdXJsLCB0aHVtYiBpbiBtYXRjaDoJCgkJdHJ5OgoJCQl4bWxfcGxheWxpc3QobmFtZSwgdXJsLCB0aHVtYikKCQlleGNlcHQ6CgkJCXBhc3MKCQkJCQpkZWYgbTN1X3BsYXlsaXN0KG5hbWUsIHVybCwgdGh1bWIpOgkKCW5hbWUgPSByZS5zdWIoJ1xzKycsICcgJywgbmFtZSkuc3RyaXAoKQkJCQoJdXJsID0gdXJsLnJlcGxhY2UoJyInLCAnICcpLnJlcGxhY2UoJyZhbXA7JywgJyYnKS5zdHJpcCgpCglpZiAoJ3lvdXR1YmUuY29tL3VzZXIvJyBpbiB1cmwpIG9yICgneW91dHViZS5jb20vY2hhbm5lbC8nIGluIHVybCkgb3IgKCd5b3V0dWJlL3VzZXIvJyBpbiB1cmwpIG9yICgneW91dHViZS9jaGFubmVsLycgaW4gdXJsKToKCQlpZiAndHZnLWxvZ28nIGluIHRodW1iOgoJCQl0aHVtYiA9IHJlLmNvbXBpbGUobTN1X3RodW1iX3JlZ2V4KS5maW5kYWxsKHN0cih0aHVtYikpWzBdLnJlcGxhY2UoJyAnLCAnJTIwJykJCQkKCQkJYWRkX2RpcihuYW1lLCB1cmwsICcnLCB0aHVtYiwgdGh1bWIpCQkJCgkJZWxzZToJCgkJCWFkZF9kaXIobmFtZSwgdXJsLCAnJywgaWNvbiwgZmFuYXJ0KQoJZWxzZToKCQlpZiAneW91dHViZS5jb20vd2F0Y2g/dj0nIGluIHVybDoKCQkJdXJsID0gJ3BsdWdpbjovL3BsdWdpbi52aWRlby55b3V0dWJlL3BsYXkvP3ZpZGVvX2lkPSVzJyAlICh1cmwuc3BsaXQoJz0nKVstMV0pCgkJZWxpZiAnZGFpbHltb3Rpb24uY29tL3ZpZGVvLycgaW4gdXJsOgoJCQl1cmwgPSB1cmwuc3BsaXQoJy8nKVstMV0uc3BsaXQoJ18nKVswXQoJCQl1cmwgPSAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmRhaWx5bW90aW9uX2NvbS8/bW9kZT1wbGF5VmlkZW8mdXJsPSVzJyAlIHVybAkKCQllbHNlOgkJCQoJCQl1cmwgPSB1cmwKCQlpZiAndHZnLWxvZ28nIGluIHRodW1iOgkJCQkKCQkJdGh1bWIgPSByZS5jb21waWxlKG0zdV90aHVtYl9yZWdleCkuZmluZGFsbChzdHIodGh1bWIpKVswXS5yZXBsYWNlKCcgJywgJyUyMCcpCgkJCWFkZF9saW5rKG5hbWUsIHVybCwgMSwgdGh1bWIsIHRodW1iKQkJCQoJCWVsc2U6CQkJCQoJCQlhZGRfbGluayhuYW1lLCB1cmwsIDEsIGljb24sIGZhbmFydCkJCgkJCQkJCmRlZiB4bWxfcGxheWxpc3QobmFtZSwgdXJsLCB0aHVtYik6CgluYW1lID0gcmUuc3ViKCdccysnLCAnICcsIG5hbWUpLnN0cmlwKCkJCQkKCXVybCA9IHVybC5yZXBsYWNlKCciJywgJyAnKS5yZXBsYWNlKCcmYW1wOycsICcmJykuc3RyaXAoKQoJaWYgKCd5b3V0dWJlLmNvbS91c2VyLycgaW4gdXJsKSBvciAoJ3lvdXR1YmUuY29tL2NoYW5uZWwvJyBpbiB1cmwpIG9yICgneW91dHViZS91c2VyLycgaW4gdXJsKSBvciAoJ3lvdXR1YmUvY2hhbm5lbC8nIGluIHVybCk6CgkJaWYgbGVuKHRodW1iKSA+IDA6CQoJCQlhZGRfZGlyKG5hbWUsIHVybCwgJycsIHRodW1iLCB0aHVtYikJCQkKCQllbHNlOgkKCQkJYWRkX2RpcihuYW1lLCB1cmwsICcnLCBpY29uLCBmYW5hcnQpCgllbHNlOgoJCWlmICd5b3V0dWJlLmNvbS93YXRjaD92PScgaW4gdXJsOgoJCQl1cmwgPSAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvcGxheS8/dmlkZW9faWQ9JXMnICUgKHVybC5zcGxpdCgnPScpWy0xXSkKCQllbGlmICdkYWlseW1vdGlvbi5jb20vdmlkZW8vJyBpbiB1cmw6CgkJCXVybCA9IHVybC5zcGxpdCgnLycpWy0xXS5zcGxpdCgnXycpWzBdCgkJCXVybCA9ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZGFpbHltb3Rpb25fY29tLz9tb2RlPXBsYXlWaWRlbyZ1cmw9JXMnICUgdXJsCQoJCWVsc2U6CQkJCgkJCXVybCA9IHVybAoJCWlmIGxlbih0aHVtYikgPiAwOgkJCgkJCWFkZF9saW5rKG5hbWUsIHVybCwgMSwgdGh1bWIsIHRodW1iKQkJCQoJCWVsc2U6CQkJCgkJCWFkZF9saW5rKG5hbWUsIHVybCwgMSwgaWNvbiwgZmFuYXJ0KQkKCQpkZWYgcGxheV92aWRlbyh1cmwpOgoJbWVkaWFfdXJsID0gdXJsCglpdGVtID0geGJtY2d1aS5MaXN0SXRlbShuYW1lLCBwYXRoID0gbWVkaWFfdXJsKQoJeGJtY3BsdWdpbi5zZXRSZXNvbHZlZFVybChpbnQoc3lzLmFyZ3ZbMV0pLCBUcnVlLCBpdGVtKQoJcmV0dXJuCgpkZWYgZ2V0X3BhcmFtcygpOgoJcGFyYW0gPSBbXQoJcGFyYW1zdHJpbmcgPSBzeXMuYXJndlsyXQoJaWYgbGVuKHBhcmFtc3RyaW5nKT49IDI6CgkJcGFyYW1zID0gc3lzLmFyZ3ZbMl0KCQljbGVhbmVkcGFyYW1zID0gcGFyYW1zLnJlcGxhY2UoJz8nLCAnJykKCQlpZiAocGFyYW1zW2xlbihwYXJhbXMpLTFdID09ICcvJyk6CgkJCXBhcmFtcyA9IHBhcmFtc1swOmxlbihwYXJhbXMpLTJdCgkJcGFpcnNvZnBhcmFtcyA9IGNsZWFuZWRwYXJhbXMuc3BsaXQoJyYnKQoJCXBhcmFtID0ge30KCQlmb3IgaSBpbiByYW5nZShsZW4ocGFpcnNvZnBhcmFtcykpOgoJCQlzcGxpdHBhcmFtcyA9IHt9CgkJCXNwbGl0cGFyYW1zID0gcGFpcnNvZnBhcmFtc1tpXS5zcGxpdCgnPScpCgkJCWlmIChsZW4oc3BsaXRwYXJhbXMpKSA9PSAyOgoJCQkJcGFyYW1bc3BsaXRwYXJhbXNbMF1dID0gc3BsaXRwYXJhbXNbMV0KCXJldHVybiBwYXJhbQoKZGVmIGFkZF9kaXIobmFtZSwgdXJsLCBtb2RlLCBpY29uaW1hZ2UsIGZhbmFydCk6Cgl1ID0gc3lzLmFyZ3ZbMF0gKyAiP3VybD0iICsgdXJsbGliLnF1b3RlX3BsdXModXJsKSArICImbW9kZT0iICsgc3RyKG1vZGUpICsgIiZuYW1lPSIgKyB1cmxsaWIucXVvdGVfcGx1cyhuYW1lKSArICImaWNvbmltYWdlPSIgKyB1cmxsaWIucXVvdGVfcGx1cyhpY29uaW1hZ2UpCglvayA9IFRydWUKCWxpeiA9IHhibWNndWkuTGlzdEl0ZW0obmFtZSwgaWNvbkltYWdlID0gIkRlZmF1bHRGb2xkZXIucG5nIiwgdGh1bWJuYWlsSW1hZ2UgPSBpY29uaW1hZ2UpCglsaXouc2V0SW5mbyggdHlwZSA9ICJWaWRlbyIsIGluZm9MYWJlbHMgPSB7ICJUaXRsZSI6IG5hbWUgfSApCglsaXouc2V0UHJvcGVydHkoJ2ZhbmFydF9pbWFnZScsIGZhbmFydCkKCWlmICgneW91dHViZS5jb20vdXNlci8nIGluIHVybCkgb3IgKCd5b3V0dWJlLmNvbS9jaGFubmVsLycgaW4gdXJsKSBvciAoJ3lvdXR1YmUvdXNlci8nIGluIHVybCkgb3IgKCd5b3V0dWJlL2NoYW5uZWwvJyBpbiB1cmwpOgoJCXUgPSAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvJXMvJXMvJyAlICh1cmwuc3BsaXQoICcvJyApWy0yXSwgdXJsLnNwbGl0KCAnLycgKVstMV0pCgkJb2sgPSB4Ym1jcGx1Z2luLmFkZERpcmVjdG9yeUl0ZW0oaGFuZGxlID0gaW50KHN5cy5hcmd2WzFdKSwgdXJsID0gdSwgbGlzdGl0ZW0gPSBsaXosIGlzRm9sZGVyID0gVHJ1ZSkKCQlyZXR1cm4gb2sJCQoJb2sgPSB4Ym1jcGx1Z2luLmFkZERpcmVjdG9yeUl0ZW0oaGFuZGxlID0gaW50KHN5cy5hcmd2WzFdKSwgdXJsID0gdSwgbGlzdGl0ZW0gPSBsaXosIGlzRm9sZGVyID0gVHJ1ZSkKCXJldHVybiBvawoKZGVmIGFkZF9saW5rKG5hbWUsIHVybCwgbW9kZSwgaWNvbmltYWdlLCBmYW5hcnQpOgoJdSA9IHN5cy5hcmd2WzBdICsgIj91cmw9IiArIHVybGxpYi5xdW90ZV9wbHVzKHVybCkgKyAiJm1vZGU9IiArIHN0cihtb2RlKSArICImbmFtZT0iICsgdXJsbGliLnF1b3RlX3BsdXMobmFtZSkgKyAiJmljb25pbWFnZT0iICsgdXJsbGliLnF1b3RlX3BsdXMoaWNvbmltYWdlKQkKCWxpeiA9IHhibWNndWkuTGlzdEl0ZW0obmFtZSwgaWNvbkltYWdlID0gIkRlZmF1bHRWaWRlby5wbmciLCB0aHVtYm5haWxJbWFnZSA9IGljb25pbWFnZSkKCWxpei5zZXRJbmZvKCB0eXBlID0gIlZpZGVvIiwgaW5mb0xhYmVscyA9IHsgIlRpdGxlIjogbmFtZSB9ICkKCWxpei5zZXRQcm9wZXJ0eSgnZmFuYXJ0X2ltYWdlJywgZmFuYXJ0KQoJbGl6LnNldFByb3BlcnR5KCdJc1BsYXlhYmxlJywgJ3RydWUnKSAKCW9rID0geGJtY3BsdWdpbi5hZGREaXJlY3RvcnlJdGVtKGhhbmRsZSA9IGludChzeXMuYXJndlsxXSksIHVybCA9IHUsIGxpc3RpdGVtID0gbGl6KSAgCgkJCnBhcmFtcyA9IGdldF9wYXJhbXMoKQp1cmwgPSBOb25lCm5hbWUgPSBOb25lCm1vZGUgPSBOb25lCmljb25pbWFnZSA9IE5vbmUKCnRyeToKCXVybCA9IHVybGxpYi51bnF1b3RlX3BsdXMocGFyYW1zWyJ1cmwiXSkKZXhjZXB0OgoJcGFzcwp0cnk6CgluYW1lID0gdXJsbGliLnVucXVvdGVfcGx1cyhwYXJhbXNbIm5hbWUiXSkKZXhjZXB0OgoJcGFzcwp0cnk6Cgltb2RlID0gaW50KHBhcmFtc1sibW9kZSJdKQpleGNlcHQ6CglwYXNzCnRyeToKCWljb25pbWFnZSA9IHVybGxpYi51bnF1b3RlX3BsdXMocGFyYW1zWyJpY29uaW1hZ2UiXSkKZXhjZXB0OgoJcGFzcyAgCgpwcmludCAiTW9kZTogIiArIHN0cihtb2RlKQpwcmludCAiVVJMOiAiICsgc3RyKHVybCkKcHJpbnQgIk5hbWU6ICIgKyBzdHIobmFtZSkKcHJpbnQgImljb25pbWFnZTogIiArIHN0cihpY29uaW1hZ2UpCQkKCmlmIG1vZGUgPT0gTm9uZSBvciB1cmwgPT0gTm9uZSBvciBsZW4odXJsKSA8IDE6CgltYWluKCkKCmVsaWYgbW9kZSA9PSAxOgoJcGxheV92aWRlbyh1cmwpCgplbGlmIG1vZGUgPT0gMjoKCW0zdV9vbmxpbmUoKQoJCmVsaWYgbW9kZSA9PSAzOgoJbTN1X2xvY2FsKCkKCQplbGlmIG1vZGUgPT0gNDoKCXhtbF9vbmxpbmUoKQoJCmVsaWYgbW9kZSA9PSA1OgoJeG1sX2xvY2FsKCkJCgplbGlmIG1vZGUgPT0gOTk6CglzZWFyY2goKQoJCnhibWNwbHVnaW4uZW5kT2ZEaXJlY3RvcnkocGx1Z2luX2hhbmRsZSk="))