{{- define "webapp.name" -}}
webapp
{{- end }}

{{- define "webapp.fullname" -}}
{{ .Release.Name }}-webapp
{{- end }}
