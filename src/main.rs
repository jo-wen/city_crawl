use csv::ReaderBuilder;
use reqwest;
use std::error::Error;
use std::fs::File;
use tokio;

#[derive(Debug, serde::Deserialize)]
struct City {
    city: String,
}

async fn check_website(url: &str) -> bool {
    match reqwest::get(url).await {
        Ok(response) => response.status().is_success(),
        Err(_) => false,
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Open and read the CSV file
    let file = File::open("lib/cities.csv")?;
    let mut rdr = ReaderBuilder::new().has_headers(true).from_reader(file);

    // Process each row in the CSV file
    for result in rdr.deserialize() {
        let city: City = result?;
        let city_name = &city.city;

        // Check for domains with both http and https asynchronously
        let has_com_http = check_website(&format!("http://{}.com", city_name)).await;
        let has_com_https = check_website(&format!("https://{}.com", city_name)).await;

        let has_us_http = check_website(&format!("http://{}.us", city_name)).await;
        let has_us_https = check_website(&format!("https://{}.us", city_name)).await;

        let has_gov_http = check_website(&format!("http://{}.gov", city_name)).await;
        let has_gov_https = check_website(&format!("https://{}.gov", city_name)).await;

        // Build the report
        if (has_com_http || has_com_https || has_us_http || has_us_https) && !(has_gov_http || has_gov_https) {
            println!("City: {}", city_name);
            if has_com_http || has_com_https {
                println!(" - Has valid .com domain");
            }
            if has_us_http || has_us_https {
                println!(" - Has valid .us domain");
            }
            println!("------------------------");
        }
    }

    Ok(())
}

