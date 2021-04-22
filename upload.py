import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('jimryan1.jpeg','UVA President'),
      ('jimryan2.jpeg','UVA President'),
      ('jimryan3.jpeg','UVA President'),
      ('timsands1.jpeg','VTech President'),
      ('timsands2.jpeg','VTech President'),
      ('timsands3.jpeg','VTech President')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('rz5sc-cs4740-pa5','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'Name':image[1]}
                    )
