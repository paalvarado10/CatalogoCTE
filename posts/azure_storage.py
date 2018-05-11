# -*- coding: utf-8 -*-
from azure.storage.blob import BlockBlobService
from decouple import config


# Guardar en AZURE y retorna la url de acceso al archivo.
def guardar_archivo(archivo, nombre):
    # PUNTO DE CONEXIÓN DE SERVICIO BLOB PRINCIPAL
    baseUrl = config('STORAGE_URL', default='')
    # Una firma de acceso compartido (SAS) es un identificador URI que concede derechos de acceso
    # limitados a recursos de Azure Storage
    sas = config('SAS', default='')
    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name=config('ACCOUNT_NAME', default=''),
                                          account_key=config('ACCOUNT_KEY', default=''))

    # Upload the created file, use local_file_name for the blob name
    block_blob_service.create_blob_from_bytes('pictures', nombre, archivo)

    return baseUrl + nombre + sas
