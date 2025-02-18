Here’s a **simple README** that outlines the main steps for automating Cloud Run deployment using **Cloud Build** and **Cloud Deploy**.

---

### **🚀 Automating Cloud Run Deployment with Cloud Build & Cloud Deploy**  

This guide walks you through setting up **CI/CD automation** to deploy a containerized application to **Cloud Run** in both **Dev** and **Prod** environments.  

---

## **🔹 Prerequisites**
1. **Google Cloud Project** with **Billing Enabled**  
2. **Cloud Run, Cloud Build, Cloud Deploy, and Artifact Registry APIs enabled**  
3. **IAM Permissions**: Ensure your user has the required roles:
   - `roles/cloudbuild.builds.editor`
   - `roles/clouddeploy.admin`
   - `roles/run.admin`
   - `roles/artifactregistry.writer`

---

## **🛠️ Step 1: Create an Artifact Registry**  
Store the container images.  

```sh
gcloud artifacts repositories create training-repo \
    --repository-format=docker \
    --location=us-central1
```

---

## **📦 Step 2: Configure Cloud Build**  
- **Builds & pushes** the container image  
- **Triggers Cloud Deploy** to release the new version  

Define a `cloudbuild.yaml` and store it in your repository.

---

## **🚀 Step 3: Configure Cloud Deploy**  
- **Manages Dev & Prod deployments**  
- **Dev deploys automatically, Prod requires approval**  

Create `clouddeploy.yaml` and apply the pipeline:

```sh
gcloud deploy apply --file clouddeploy.yaml --region=us-central1
```

---

## **📤 Step 4: Push Code & Trigger CI/CD**  
Once you push changes to your repository, **Cloud Build** will:
1. **Build the image**  
2. **Push to Artifact Registry**  
3. **Trigger Cloud Deploy**  
4. **Deploy to Cloud Run (Dev auto, Prod manual approval)**  

Trigger a release manually (if needed):  

```sh
gcloud deploy releases create release-001 \
    --delivery-pipeline=delivery-prod-pipeline \
    --region=us-central1 \
    --images=my-app=us-central1-docker.pkg.dev/$PROJECT_ID/training-repo/py-helloworld:latest
```

---

## **✅ Step 5: Approve Production Deployment**  
Approve the deployment to **Prod** (after testing in **Dev**):

```sh
gcloud deploy rollouts approve rollout-id \
    --delivery-pipeline=delivery-prod-pipeline \
    --region=us-central1
```

---

## **🎉 Done!**