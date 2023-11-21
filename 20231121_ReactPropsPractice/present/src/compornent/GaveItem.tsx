interface GaveItemProps {
    item: string;
}

  export default function GaveItem(props: GaveItemProps) {
    const label = "あなたが私にくれたもの";
    return (
      <div>
        <span>
          {label}　{props.item}
        </span>
      </div>
    );
}
