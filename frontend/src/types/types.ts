export interface Ingredient {
  name: string;
  unit: string;
  quantity: string;
}

export interface Recipe {
  name: string;
  ingredients: Ingredient[];
  steps: string[];
  total_time_minutes: number;
  person_count: number;
}

export interface OutputProps {
  data: Recipe | undefined;
  onBack: () => void;
}

export const sampleRecipe: Recipe = {
  name: "Chocolate Chip Cookies",
  ingredients: [
    { name: "Flour", unit: "cups", quantity: "2.5" },
    { name: "Baking Soda", unit: "tsp", quantity: "1" },
    { name: "Salt", unit: "tsp", quantity: "0.5" },
    { name: "Butter", unit: "cups", quantity: "1" },
    { name: "Sugar", unit: "cups", quantity: "0.75" },
    { name: "Brown Sugar", unit: "cups", quantity: "0.75" },
    { name: "Vanilla Extract", unit: "tsp", quantity: "1" },
    { name: "Eggs", unit: "", quantity: "2" },
    { name: "Chocolate Chips", unit: "cups", quantity: "2" },
  ],
  steps: [
    "Preheat oven to 350 degrees F.",
    "Mix dry ingredients in a bowl.",
    "Cream together butter and sugars.",
    "Beat in vanilla extract and eggs.",
    "Gradually blend in dry ingredients.",
    "Stir in the chocolate chips.",
    "Drop by spoonfuls onto ungreased cookie sheets.",
    "Bake for 8 to 10 minutes, until golden brown.",
  ],
  total_time_minutes: 30,
  person_count: 4,
};
