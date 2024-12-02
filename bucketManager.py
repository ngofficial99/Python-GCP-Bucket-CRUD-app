import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

class GCPBucketManager:
    def __init__(self, bucket_name):
        # Initialize storage client using credentials from environment
        self.storage_client = storage.Client()
        self.bucket_name = bucket_name
        self.bucket = self.storage_client.bucket(bucket_name)

    def list_objects(self):
        """List all objects in the bucket."""
        blobs = self.storage_client.list_blobs(self.bucket_name)
        print(f"Objects in bucket '{self.bucket_name}':")
        for blob in blobs:
            print(f"- {blob.name}")

    def upload_object(self, local_file_path, destination_blob_name=None):
        """
        Upload a file to the bucket.
        
        :param local_file_path: Path to the local file to upload
        :param destination_blob_name: Optional name in the bucket (defaults to filename)
        """
        # If no destination name provided, use the filename
        if destination_blob_name is None:
            destination_blob_name = os.path.basename(local_file_path)
        
        # Upload the file
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)
        
        print(f"File {local_file_path} uploaded to {destination_blob_name}")

    def delete_object(self, blob_name):
        """
        Delete an object from the bucket.
        
        :param blob_name: Name of the object to delete
        """
        blob = self.bucket.blob(blob_name)
        blob.delete()
        print(f"Object {blob_name} deleted from bucket")

def main():
   
    bucket_name = os.getenv('GCP_BUCKET_NAME')
    
    if not bucket_name:
        print("Please set GCP_BUCKET_NAME in your .env file")
        return
    
    bucket_manager = GCPBucketManager(bucket_name)
    
    while True:
        print("\n--- GCP Bucket Management ---")
        print("1. List Objects")
        print("2. Upload Object")
        print("3. Delete Object")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            bucket_manager.list_objects()
        
        elif choice == '2':
            file_path = input("Enter the full path of the file to upload: ")
            if os.path.exists(file_path):
                destination_name = input("Enter destination name in bucket (optional, press Enter to use filename): ")
                bucket_manager.upload_object(file_path, destination_name if destination_name else None)
            else:
                print("File does not exist!")
        
        elif choice == '3':
            object_name = input("Enter the name of the object to delete: ")
            bucket_manager.delete_object(object_name)
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()