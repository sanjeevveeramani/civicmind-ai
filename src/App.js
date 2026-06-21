import { useState } from "react";
import { Layout, Typography } from "antd";
import IntakeForm from "./pages/IntakeForm";
import ScoreResults from "./pages/ScoreResults";
import GapAnalysis from "./pages/GapAnalysis";

const { Header, Content } = Layout;
const { Title, Text } = Typography;

function App() {
  const [page, setPage] = useState("intake");
  const [results, setResults] = useState(null);

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Header style={{ background: "#0f3d5e" }}>
        <Title level={3} style={{ color: "white", margin: 0 }}>
          CivicMind AI
        </Title>
      </Header>

      <Content style={{ maxWidth: 1100, width: "100%", margin: "0 auto", padding: 24 }}>
        <Title>Dual-Path AI Readiness Assessment</Title>
        <Text>Intake → Path A + Path B → Confidence Arbitrator → Gap Analysis</Text>

        {page === "intake" && (
          <IntakeForm setResults={setResults} setPage={setPage} />
        )}

        {page === "results" && (
          <ScoreResults data={results} setPage={setPage} />
        )}

        {page === "gaps" && <GapAnalysis data={results} setPage={setPage} />}
      </Content>
    </Layout>
  );
}

export default App;