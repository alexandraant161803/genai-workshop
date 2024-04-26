import { useQuery } from "react-query";
import { healthCheck } from "../services/RecipeService";

function HealthStatus() {
  const { isLoading, error } = useQuery("healthCheck", healthCheck);

  if (isLoading) return <div className=" text-primary">Checking connection to backend</div>;

  if (error) return <div className="text-primary">Unable to connect to backend</div>;

  return (
    <div className="text-primary">
      Connected to backend
    </div>
  );
}

export default HealthStatus;
