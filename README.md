# Mini Assessment

## Project Structure

This project was developed locally, tested in Docker containers, and finally deployed on AWS.

### Deployment
- **Database:** PostgreSQL on AWS RDS  
- **App Hosting:** Django deployed on AWS ECS  
- **Endpoints:**  
  - Admin panel: `http://<your-aws-ec2-ip>:8000/admin`  
  - API conversations: `http://<your-aws-ec2-ip>:8000/api/conversations/`  
  - Vegetarian/Vegan filter: `http://<your-aws-ec2-ip>:8000/api/conversations/get_vegeterians/`  

(*Note: replace `<your-aws-ec2-ip>` with your actual server IP*)  

---

### ChatBotApp

Inside the `chatBotApp` folder, you’ll find the `chatbot.py` script.  
Run it with:  
```bash
python chatbot.py
